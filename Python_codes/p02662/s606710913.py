import sys
def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(10**9)
mod = 998244353

def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    
    """
    maspyさんの多項式解法も試してみる。
    例えばA = [2, 2, 4]の場合、
        f({1, 2, 3}) = [x^S](1 + x^2)(1 + x^2)(1 + x^4)
        f({1, 2})    = [x^S](1 + x^2)(1 + x^2)
    よって求める答えはf_i = (1 + x^{A[i]})として
        [x^S](f_1 f_2 f_3 + f_1 f_2 + f_2 f_3 + f_3 f_1 + f_1 + f_2 + f_3)
    となる。
    さらにS >= 1なのでこれに1を足しても結果は変わらない。なので因数分解して
        [x^S](1 + f_1)(1 + f_2)(1 + f_3)
    を求めればよい。
    """

    poly = [0] * (S + 1) # poly[i] = (x^iの係数)
    poly[0] = 1
    for a in A:
        # poly *= (2 + x^a)
        poly2 = [poly[i] * 2 % mod for i in range(S + 1)]
        for i in range(S + 1):
            if i + a <= S:
                poly2[i + a] += poly[i]
                poly2[i + a] %= mod
        poly = poly2
    print(poly[S])
    

if __name__ == "__main__":
    main()
