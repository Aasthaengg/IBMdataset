ans=0
c=[list(map(int,input().split())) for _ in range(int(input()))]
for a,b in c[::-1]:    
    if (a+ans)%b:
        ans+=(-a-ans)%b
print(ans)