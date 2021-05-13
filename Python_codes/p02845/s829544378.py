from collections import Counter
N = int(input())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7
ans = 1
cnt = [0] * N
for i, a in enumerate(A):
    cnt[a] += 1
    if a == 0:
        ans *= 4 - cnt[a]
    else:
        ans *= max(0, cnt[a-1]-cnt[a]+1)
    ans %= MOD

print(ans)
