L=int(input())
ans=0
for j in range(1,1000*L+1):
    i=j/1000
    ans=max(ans,i*i*(L-2*i))
print(ans)