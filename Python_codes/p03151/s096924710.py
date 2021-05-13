n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=[]

for i in range(n):
    c.append(a[i]-b[i])

c=sorted(c)

i=0
minus=0
ans=0
while c[i]<0:
    minus+=c[i]
    i+=1
    ans+=1

i=n-1
plus=0
while plus+minus<0:
    if c[i]<=0:
        print(-1)
        exit(0)
    plus+=c[i]
    i-=1
    ans+=1

print(ans)