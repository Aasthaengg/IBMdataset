N=int(input())
L=list(map(int,input().split()))
L.sort()
ans=0
for i in range(N):
    for j in range(i+1,N):
        if L[i]==L[j]:
            continue
        for k in range(j+1,N):
            if L[j]==L[k]:
                continue
            if L[i]+L[j]>L[k]:
                ans+=1
print(ans)
