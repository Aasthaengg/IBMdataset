n=int(input())
p=list(map(int,input().split()))
L=[]*3
ans=0
for i in range(n-2):
    L=p[i:i+3]
    L.sort()
    if L[1]==p[i+1]:
        ans+=1
print(ans)