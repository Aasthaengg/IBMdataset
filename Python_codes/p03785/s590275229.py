import sys
input = sys.stdin.readline

N, C, K = map(int, input().split())
T = [int(input()) for i in range(N)]
T.sort()
ans = 0
cnt = 1
mn = T[0]
for i in range(1,N):
    if cnt == C or mn+K < T[i]:
        ans += 1
        cnt = 1
        mn = T[i]
    else:
        cnt += 1
if cnt > 0:
    ans += 1
print(ans)
