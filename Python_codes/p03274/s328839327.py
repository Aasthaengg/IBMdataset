n, k = map(int,input().split())
x_l = list(map(int,input().split()))

ans = float('inf')
for i in range(n-k+1):
    if x_l[i] * x_l[i+k-1] < 0:
        tmp = min(abs(x_l[i]), abs(x_l[i+k-1])) * 2 + max(abs(x_l[i]), abs(x_l[i+k-1]))
    elif x_l[i] < 0:
        tmp = abs(x_l[i])
    else:
        tmp = abs(x_l[i+k-1])
    ans = min(ans, tmp)

print(ans)