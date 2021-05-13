S,W=list(map(int,input().split()))

if S <= W:
    ans = 'unsafe'
else:
    ans = 'safe'
    
print(ans)