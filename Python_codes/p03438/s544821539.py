N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

d=[]
for i in range(N):
    d.append(a[i]-b[i])

cnt=-sum(d)
p=0
n=0
for j in range(N):
    if d[j]>0:
        p+=d[j]
    if d[j]<0:
        n+=-d[j]-(-d[j])%2
if n>=p*2:
    print("Yes")
else:
    print("No")