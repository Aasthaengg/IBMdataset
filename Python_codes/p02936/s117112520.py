from collections import deque
n,q=map(int,input().split())
num=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    num[a-1].append(b)
    num[b-1].append(a)
ans=[0]*n
for i in range(q):
    p,x=map(int,input().split())
    ans[p-1]+=x
queue=deque()
queue.append(0)
seen=[False]*n
for i in range(n):
    if len(queue)==0:
        break
    num1=queue.popleft()
    seen[num1]=True
    num2=num[num1]
    for j in range(len(num2)):
        if seen[num2[j]-1]==False:
            ans[num2[j]-1]+=ans[num1]
            queue.append(num2[j]-1)
for i in ans:
    print(i)
