import sys
import math
sys.setrecursionlimit(1000000) # 再帰上限を増やす

def calc_combi(n, m, mod=1000000007):
    """ nCmの組み合わせ数を数える """
    if n - m < m:
        return calc_combi(n, n - m)

    ans_mull, ans_div = 1, 1
    for i in range(m):
        ans_mull *= (n - i)
        ans_div *= (i + 1)
        ans_mull %= mod
        ans_div %= mod
    ans = ans_mull * pow(ans_div, mod - 2, mod) % mod
    return ans

def main():
    input = sys.stdin.readline  # 文字列に対してinputした場合は、rstripするのを忘れずに！
    N, M = map(int, input().rstrip().split())
    mod = 1000000007

    ans = 1
    for i in range(2, math.ceil(math.sqrt(M))):
        if M % i == 0:
            count = 0
            while M % i == 0:
                M /= i
                count += 1
            ans *= calc_combi(count + N - 1, N - 1, mod)
            ans %= mod
    if M != 1:
        ans *= calc_combi(N, 1, mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()