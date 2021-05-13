n=int(input())
ans=0
for i in range(n,n+200):
    N=str(i)
    if N[0]==N[1]==N[2]:
        ans=i
        break
print(ans)