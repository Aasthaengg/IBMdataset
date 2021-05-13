from collections import deque

M,K = map(int,input().split())
if K >= 2**M or M==K==1:
    print(-1)
    exit()
if M == 1:
    print(0,0,1,1)
    exit()

ans = deque([K])
for n in range(2**M):
    if n==K: continue
    ans.append(n)
    ans.appendleft(n)
ans.appendleft(K)
print(*ans)