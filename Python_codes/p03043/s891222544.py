import math

n, k = map(int, input().split())

tmp = []
for i in range(1, n + 1):
    if i < k:
        num = (-1 * math.log2(k / i)) // 1 * -1 
        tmp.append(num)
    else:
        tmp.append(0)
        
ans = 0
for i in range(n):
    ans += 2**(tmp[0] - tmp[i])

print(ans / (n * 2**tmp[0]))