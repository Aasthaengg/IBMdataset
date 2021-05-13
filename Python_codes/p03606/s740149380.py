n=int(input())
ans=0

for i in range(n):
    a,b=[int(i) for i in input().split()]
    ans+=b-a+1
    
print(ans)