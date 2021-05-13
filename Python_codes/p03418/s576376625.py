n, k = map(int, input().split())
res = 0
for b in range(k+1, n+1):
#     print("-"*10)
    if n%b == 0:
        res += (n//b) * (b-k)
#         print((n//b) * (b-k))
    else:
        res += n//b*(b-k) + max(n%b - k  + 1, 0)
        if k == 0:
            res -= 1
#         print(b, n//b*(b-k), max(n%b - k + 1, 0))
print(res)