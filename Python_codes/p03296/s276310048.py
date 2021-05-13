N=int(input())
a=list(map(int,input().split()))
b=[1]
c=1
for i in range(1,len(a)):
    if a[i-1]==a[i]:
        c+=1
        b.append(c)
    if a[i-1]!=a[i]:
        c=1
        b.append(c)
d=[]
for i in range(len(b)-1):
    if b[i]>=b[i+1]:
        d.append(b[i])
d.append(b[len(b)-1])
e=0
for i in range(len(d)):
    e+=d[i]//2
print(e)