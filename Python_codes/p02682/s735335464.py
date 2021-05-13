a,b,c,k = [int(i) for i in input().split()]
p = min(a,k)
ans = p
k -= p

if k>0:
    k-=min(b,k)
if k>0:
    ans-=min(k,c)
    
print(ans)
