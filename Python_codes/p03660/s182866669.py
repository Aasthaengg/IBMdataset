import sys
input=sys.stdin.readline
n=int(input())
from collections import deque
G=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
check=[False]*n
check[0]=True
check[n-1]=True
f_q=deque([0])
s_q=deque([n-1])
f_c=1
s_c=1
while not (len(f_q)==0 and len(s_q)==0):
    f_n=len(f_q)
    for i in range(f_n):
        now=f_q.popleft()
        for j in G[now]:
            if not check[j]:
                check[j]=True
                f_c+=1
                f_q.append(j)
    s_n=len(s_q)
    for i in range(s_n):
        now=s_q.popleft()
        for j in G[now]:
            if not check[j]:
                check[j]=True
                s_c+=1
                s_q.append(j)
if f_c>s_c:
    print('Fennec')
else:
    print('Snuke')


