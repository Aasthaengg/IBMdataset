from collections import deque

n=int(input())
a=[0]+list(map(int, input().split()))

b=deque()

for i in range(1, n+1):
    if n%2==i%2:
        b.appendleft(a[i])
    else:
        b.append(a[i])

ans=[]

for elem in b:
    ans.append(elem)

print(*ans)