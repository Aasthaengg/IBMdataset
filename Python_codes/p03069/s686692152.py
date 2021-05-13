import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    S = input()
    ans = S.count('.')
    score = ans
    for c in S:
        if c == '.':
            score -= 1
        else:
            score += 1
        ans = min(ans, score)
    print(ans)
resolve()