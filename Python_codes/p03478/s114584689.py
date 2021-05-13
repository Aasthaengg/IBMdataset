n,a,b=map(int, input().split()) 
tmp=0
ans=0

for i in range(n+1):
    for j in range(len(str(i))):
        tmp+=int(str(i)[j])
    if tmp>=a and tmp<=b:
        ans+=i
    tmp=0

print(ans)