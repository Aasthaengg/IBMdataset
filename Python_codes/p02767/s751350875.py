n=int(input())
x=list(map(int,input().split()))
ans=1000000000000
for p in range(100):
    a=0
    for i in range(n):
        a+=(x[i]-p)**2 
    if a < ans:
        ans = a

print(ans)