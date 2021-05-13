N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()
s = 0
ans = 0
for i in range(N):
    if i - s + 1 > C or T[i] - T[s] > K:
        s = i
        ans += 1
print(ans+1)
