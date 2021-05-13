 #15858750
n, m, x = map(int, input().split()) 
a = [list(map(int, input().split())) for i in range(n)]
ans = 12*(10**5) + 1

for j in range(2**n):  
    mlist = [0]*m 
    money = 0
    for k in range(n): 
        if (j >> k) & 1 == 1:
            money += a[k][0]
            for l in range(1, m+1): 
                mlist[l-1] += a[k][l]
    if min(mlist) >= x:
        ans = min(ans, money)
        
if ans == 12*(10**5) + 1 :
    print(-1)
else:
    print(ans)