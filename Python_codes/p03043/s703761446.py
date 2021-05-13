N,K=map(int,input().split())
p=0
for i in range(1,N+1):
    c=0
    while i<K:
        i*=2
        c+=1
    if c!=0:
        p+=((1/2)**c)*(1/N)
if N>=K:
    p+=(N-K+1)/N
print(p)