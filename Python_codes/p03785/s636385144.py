from collections import deque
N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
D = deque(sorted(T))
cnt = 1
ans = 1
pre = D.popleft()
flag = False
while D:
    d = D.popleft()
    cnt += 1
    if cnt > C or d - pre > K:
        cnt = 1
        pre = d
        ans += 1
print(ans)
