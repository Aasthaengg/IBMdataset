n=int(input())
a=list(map(int,input().split()))
a.sort()
c=[0]
for i in range(n):
    c.append(c[i]+a[i])
p=[0 for i in range(n)]
for i in range(n):
    if c[i]*2<a[i]:
        p[i]=1
for i in range(n):
    if p[n-i-1]:
        print(i+1)
        break
#print(a,c,p,sep='\n')