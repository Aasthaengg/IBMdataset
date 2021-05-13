n,l=map(int,input().split())
mi=10000
for i in range(n):
    m=l+i
    if mi!=min(mi,abs(m)):
        j=i
        mi=min(mi,abs(m))
#print(j,mi)
ans=0
for i in range(n):
    if i!=j:
        ans+=l+i
print(ans)
