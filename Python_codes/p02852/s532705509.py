from itertools import accumulate

N, M = map(int, input().split())
S = list(map(int, input()))
cum = list(accumulate([0] + S))
ok = [False] * (N+1)
for i in range(N):
    if S[i] == 0 and cum[i+1] - cum[max(0, i-M+1)] < min(i+1, M):
        ok[i] = True
s = N
t = N
i = N
ans = []
while t > 0:
    if s - i > M:
        if s == t:
            print(-1)
            exit()
        ans.append(s - t)
        s = t
        i = s
        continue
    if ok[i]:
        t = i
    i -= 1
ans.append(s)
print(*ans[::-1])