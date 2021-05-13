l,r,d = map(int,input().split())

ans = 0

while l<=r:

    if l%d == 0:
        
        ans+=1

    l+=1

print(ans)