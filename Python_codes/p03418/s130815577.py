n,k = map(int, input().split( ))

ans = 0

if k==0:
    print(n**2)
    exit()

for b in range(k+1,n+1):##境界の処理とか+1の有無とかが難しい
    quo = n//b
    by_rem = b-k
    ans += quo * by_rem
    
    ans += max(0, n%b-k+1)
    
    
    
print(ans) 