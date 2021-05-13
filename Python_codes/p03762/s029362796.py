n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
sx = 0
sy = 0
for i in range(1,n+1):
    sx += (x[i - 1]*(i - 1)) - (x[i - 1] * (n - i))
for s in range(1,m+1):
    sy += (y[s - 1]*(s - 1)) - (y[s - 1] * (m - s))
print(abs(sx * sy)%1000000007)