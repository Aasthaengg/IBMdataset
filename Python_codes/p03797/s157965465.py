import sys
n,m = map(int,input().split())
ans = 0

if m < 2:
    print(ans)
    sys.exit()

    
if m < 2 * n:
    ans += m // 2
    print(ans)
    
    
else:
    ans += n
    x = m - 2 * n
    ans += x//4
    print(ans)