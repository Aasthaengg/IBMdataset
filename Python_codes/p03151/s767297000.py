n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    c.append(a[i]-b[i])
c=sorted(c,reverse=1)
if sum(c)<0:
    print(-1)
    exit()
d=0
e=0
f=0
for i in range(n):
    if c[i]<0:
        d+=c[i]
        e+=1
for i in range(n):
    if f>=abs(d):
        break
    f+=c[i]
print(e+i)