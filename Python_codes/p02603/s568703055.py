n=int(input())
a=list(map(int,input().split()))

l=[]
for x in range(n-1):
    if a[x+1]==a[x]:l.append(0)
    if a[x+1]>a[x]:l.append(1)
    if a[x+1]<a[x]:l.append(-1)

for x in range(n-1):
    if l.pop(-1)==1:
        l.append(1)
        l.append(-1)
        break

m=1000
p=0
for i,x in enumerate(l):
    if x==1:
        t=m//a[i]
        m-=t*a[i]
        p+=t
    if x==-1:
        m+=p*a[i]
        p=0
print(m)