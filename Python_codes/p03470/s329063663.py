N=int(input())
d=[int(input()) for i in range(N)]
d.sort()
ans=1
for j in range(N-1):
    if d[j]!=d[j+1]:
        ans+=1
print(ans)
