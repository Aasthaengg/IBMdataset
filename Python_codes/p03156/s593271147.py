from collections import deque
N=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
ans=0
x=0
y=0
z=0
for i in range(N):
    if p[i]<=a:
        x+=1
    if a+1<=p[i]<=b:
        y+=1
    if p[i]>=b+1:
        z+=1
print(min(x,y,z))