n=int(input())
lst=[int(i) for i in input().split()]

ans=0
for i in range(n):
    p=lst[i]
    while p%2==0:
        p//=2
        ans+=1
        
print(ans)