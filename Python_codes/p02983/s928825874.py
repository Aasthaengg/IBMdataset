l,r=map(int,open(0).read().split())

if r-l>=2019:
    print(0)
    exit(0)

m=[]
for i in range(l,r+1):
    m.append(i%2019)

n=len(m)
ans=2019

for i in range(n):
    for j in range(i+1,n):
        ans=min(ans,(m[i]*m[j])%2019)
    
print(ans)