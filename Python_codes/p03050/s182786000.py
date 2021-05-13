# N//m=N%m
# (N-N%m)/m=N%m
# N=(N%m)(m+1)

n=int(input())

def make_divisor(x):
    ret=[]
    for i in range(1,int(x**.5)+1):
        q,m=divmod(x,i)
        if m==0:
            ret.append(i)
            if i==q:continue
            ret.append(q)
    return ret

ans=[]
d=make_divisor(n)

for e in d:
    if e==1:continue
    m=e-1
    k=n%m
    if k*e==n:
        ans.append(m)
print(sum(ans))