import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')

def mcomb(n, k, mod):
    def mfac(l, r, mod):
        ans = l
        for i in reversed(range(r, l)):
            ans *= i
            ans %= mod
        return ans

    A = mfac(n, n-k+1, mod)
    B = mfac(k, 1, mod)
    # B = mpow(B,mod-2,mod)
    B = pow(B, mod-2, mod)
    return A * B % mod

def solve():
    N, blue = MI()
    MOD = 1000000007
    red = N - blue
    for i in range(1, blue+1):
        # ans = comb(red+1, i) * comb(blue-1, i-1)
        """
        両端を含む赤ボールの隙間 (red+1個) に青ボールグループ (i個) を入れる場合の数.
        red = 3 のとき、 挿入候補は | a | a | a | の4つ (red+1) となる.
        これに2つの青ボールグループを入れたい場合、 comb(red+1, i) 通りになる.
        """
        if red+1 < i:
            a = 0
        else:
            a = mcomb(red+1, i, MOD)

        """
        青ボール (blue個) をiグループに分割する場合の数.
        b = 4, のとき、分割候補は b | b | b | b　の3つ (blue-1個)となる.
        i = 3, つまり3分割したい場合はこの棒を2個選べば青ボールを3分割できる.
        つまり、この棒からi-1個選べばよいので、 comb(blue-1, i-1) 通りになる.
        """
        if i-1 == 0:
            b = 1
        else:
            b = mcomb(blue-1, i-1, MOD)
        print(a * b % MOD)


if __name__ == '__main__':
    solve()
