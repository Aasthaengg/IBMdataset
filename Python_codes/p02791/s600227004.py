n=int(input())
L=list(map(int,input().split()))
ans=0
Min=2*10**5+1
for i in L:
    if i<Min:
        ans+=1
        Min=i
print(ans)