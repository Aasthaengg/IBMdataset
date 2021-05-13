def get_exp(i,m):
    c=0
    while i<m:
        i=i*2
        c+=1
    return c

n,k=map(int,input().split())
r=0
for x in range(1,n+1):
    r+=1/(n*(2**get_exp(x,k)))
    
print(r)