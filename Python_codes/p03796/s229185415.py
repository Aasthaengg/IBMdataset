n=int(input())
ans=1
for i in range(n):
    ans*=i+1
    ans=ans%1000000007
print(ans)
    
