from collections import deque
N = int(input())
A = list(map(int,input().split()))
A.sort()
if len(A) == 2:
    print(A[1]-A[0])
    print(A[1],A[0])
    exit()
posi = deque([])
nega = deque([])
for i in A:
    if i < 0:
        nega.append(i)
    else:
        posi.append(i)
ans = []
if len(posi) == 0:
    x = nega.pop()
    y = nega.pop()
    posi.append(x-y)
    ans.append([x,y])
if len(nega) == 0:
    x = posi.popleft()
    y = posi.popleft()
    nega.append(x-y)
    ans.append([x,y])

while len(posi) > 1:
    x = nega.pop()
    y = posi.pop()
    ans.append([x,y])
    nega.append(x-y)
while len(nega) > 0:
    x = posi.pop()
    y = nega.pop()
    ans.append([x,y])
    posi.append(x-y)

print(posi[0])
for i in range(N-1):
    print(' '.join(map(str,ans[i])))
