n, k = map(int, input().split())
tmp1 = n // k

if k % 2 == 0:
    tmp2 = (n + k//2) // k
else:
    tmp2 = 0

ans = tmp1 ** 3 + tmp2 ** 3

print(ans)