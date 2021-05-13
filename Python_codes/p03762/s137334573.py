n,m=map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
MOD = 10**9+7

sum_x = 0
sum_y = 0
for i in range(n):
    sum_x += (n-1-i*2)*X[i] 
for i in range(m):
    sum_y += (m-1-i*2)*Y[i]
sum_x = sum_x%MOD
sum_y = sum_y%MOD
print((sum_x*sum_y)%MOD)

