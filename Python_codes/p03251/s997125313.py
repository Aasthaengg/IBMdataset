N, M, X, Y = list(map(int,input().split()))
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x_max = max(x)
y_min = min(y)
ans = 'War'
for i in range(-100,101):
    if (X < i <= Y ) and (x_max < i <= y_min):
        ans = 'No War'
print(ans)