from collections import Counter

n,m,q = map(int,input().split())
c = [[0] * (n+1) for i in range(n+1)]
da = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    l,r = map(int,input().split())
    c[l][r] += 1

da[1][1] = c[1][1]
        
for i in range(2,n+1):
    da[1][i] = da[1][i-1] + c[1][i]    
for i in range(2,n+1):
    co = 0
    for j in range(1,n+1):
        co += c[i][j]
        da[i][j] = da[i-1][j] + co
    
for i in range(q):
    pp,qq =  map(int,input().split())
    ans = 0
    ans = da[qq][qq] - da[pp-1][qq] - da[qq][pp-1] + da[pp-1][pp-1]
    
    print(ans)