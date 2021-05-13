ans=999999999
n = int(input())
for i in range(1,n//2+1):
    x=str(i)
    y=str(n-i)
    ans=min(ans, sum(map(int, x))+sum(map(int, y)))
    
print(ans)