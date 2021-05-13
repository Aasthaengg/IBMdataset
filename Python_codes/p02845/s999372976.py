MOD = 10**9 + 7
n = int(input())
a = list(map(int,input().split()))

ka = [[0]*3 for _ in range(n+1)]

for i in range(n):
    for j in range(3):
        ka[i+1][j] = ka[i][j]
        
    for j in range(3):
        if ka[i][j] == a[i]:
            ka[i+1][j] += 1
            break
    ka[i+1].sort(reverse = True)
    
ans = 1
for i in range(n):
    mlt = 0
    for j in range(3):
        if ka[i][j] == a[i]:
            mlt += 1
            
    ans = ans * mlt % MOD
        
print(ans)