n, k = map(int, input().split())
x = list(map(int, input().split()))

res = float('inf')
for i in range(n - k + 1):
    if x[i] <= 0 and x[i+k-1] <= 0:
        res = min(res, abs(x[i]))
    elif x[i] <= 0 and x[i+k-1] >= 0:
        res = min(res, 2 * abs(x[i]) + abs(x[i+k-1]), abs(x[i])+ 2 * abs(x[i+k-1]))
    else:
        res = min(res, abs(x[i+k-1]))

print(res)