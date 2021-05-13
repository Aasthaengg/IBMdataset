import sys
input=sys.stdin.readline
n=int(input())
p=[int(input()) for _ in range(n)]
q=[0]*(n+1)
for i in range(n):
    q[p[i]]=i+1

q=q[1:]
m=0
k=1
for i in range(1,n):
    if q[i]>q[i-1]:
        k+=1
    else:
        m=max(m,k)
        k=1
m=max(m,k)
print(n-m)
