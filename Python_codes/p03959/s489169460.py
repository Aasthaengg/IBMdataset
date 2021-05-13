N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

not_fixed = [True] * N

# 矛盾のチェック
MAX = 0
for i in range(N):
    if T[i] > MAX:
        MAX = T[i]
        not_fixed[i] = False
        if T[i] > A[i]:
            print(0)
            exit()

MAX = 0
for i in reversed(range(N)):
    if A[i] > MAX:
        MAX = A[i]
        not_fixed[i] = False
        if A[i] > T[i]:
            print(0)
            exit()


MIN = [min(t, a) for t, a in zip(T, A)]
ans = 1
mod = 10 ** 9 + 7

for i in range(N):
    if not_fixed[i]:
        ans *= MIN[i]
        ans %= mod

print(ans)
