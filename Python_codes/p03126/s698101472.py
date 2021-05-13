n,m= map(int,input().split())
unti= [0] * (m+1)
ans=0
for i in range(n):
    x = list(map(int,input().split()))
    for j in range(x[0]):
        unti[x[j+1]]+=1
for i in range(m+1):
    if unti[i] == n:
        ans+=1
print(ans)