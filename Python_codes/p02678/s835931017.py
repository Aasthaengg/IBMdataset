import math, sys
from collections import deque
N , M = list(map(int, input().split()))

Es = [[] for _ in range(N+1)]
for i in range(M):
    A , B = list(map(int, input().split()))
    Es[A].append(B)
    Es[B].append(A)

used = [False]*(N+1)
used[1] = True

ans = [-1]*(N+1)

cand = deque([1])
while len(cand)>0:
    tar = cand.popleft()
    for each in Es[tar]:
        if used[each]:
            continue
        cand.append(each)
        ans[each]=tar
        used[each]= True

print("Yes")
for i in range(2,N+1):
    print(ans[i])
