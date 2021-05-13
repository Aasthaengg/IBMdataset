N=int(input())
d=[int(s) for s in input().split()]
ans=0
for i in range(N-2):
    if d[i]<d[i+1]<d[i+2] or d[i+2]<d[i+1]<d[i]:
        ans+=1
print(ans)