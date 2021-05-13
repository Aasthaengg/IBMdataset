N,K=map(int,input().split())
A=list(map(int,input().split()))
def divisor(n):
    d0=[]
    d1=[]
    for i in range(1,int(n**.5)+1):
        x,y=divmod(n,i)
        if y==0:
            d0.append(i)
            d1.append(x)
    if d1[-1]==d0[-1]:
        d1=d1[:-1]
    return d0+d1[::-1]
D=divisor(sum(A))
r=1
for d in D[::-1]:
    x=sorted([a%d for a in A])
    for i in range(len(A)-1):
        x[i+1]+=x[i]
    if x[-1]%d==0 and x[-1-x[-1]//d]<=K:
        r=d
        break
print(r)