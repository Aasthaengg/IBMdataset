n,k = map(int,input().split())

if n%2 == 0:
    cnt = n//2
else:
    cnt = n//2 + 1
    
if cnt >= k:
    print("YES")
else:
    print("NO")