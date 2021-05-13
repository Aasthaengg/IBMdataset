x =int(input())

ans=0
sum=0

for i in range(0,50000):
    sum+=i
    if sum>=x:
        break
    
    ans+=1

print(ans)
