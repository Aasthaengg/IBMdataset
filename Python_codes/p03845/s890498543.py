n=int(input())
t=list(map(int,input().split()))
m=int(input())
p=[]
x=[]
for i in range(m):
    p1,x1=map(int,input().split())
    p.append(p1)
    x.append(x1)
a=0
for i in range(n):
    a+=t[i]
for i in range(m):
    print(a-t[p[i]-1]+x[i])