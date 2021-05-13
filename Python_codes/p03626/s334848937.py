import sys

sys.setrecursionlimit(10000)
INF = float('inf')

MOD = 1000000007

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

ans = 1
# 次横だったら掛ける何通りするか
next_h = 6
# 次縦だったら
next_v = 3
i = 0
while i < N:
    s, t = S[i], T[i]
    if s != t:
        # 横
        ans *= next_h
        next_h = 3
        next_v = 1
        i += 2
    else:
        # 縦
        ans *= next_v
        next_h = 2
        next_v = 2
        i += 1
    ans %= MOD

print(ans)
