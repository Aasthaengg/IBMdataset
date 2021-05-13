from collections import deque
N=int(input())
if N==1:
    print("Yes")
    print(2)
    print(1,1)
    print(1,1)
    exit()

# 1569   127 10   2368   3479   458 10  
# 1234      156 7      2589      36810      47910
#2*3  3*4 4*5
size=None
for i in range(1,N):
    if i*(i+1)==N*2:
        size=i
        groups=i+1
if size is None:
    print("No")
    exit()

ans=[[] for _ in range(groups)]
first=deque(list(range(1,N+1)))

#second=deque(list(range(1,N+1)))

for i in range(groups):
    to_idx=i+1
    while len(ans[i])<size:
        x=first.popleft()
        ans[i].append(x)
        #print(to_idx)
        ans[to_idx].append(x)
        to_idx+=1

print("Yes")
print(len(ans))
for s in ans:
    print(len(s), *s)
