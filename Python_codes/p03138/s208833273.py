import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
log2K = int(math.log2(10**12))+1
count_bit = [0 for i in range(log2K)]
for ai in A:
    for i in range(log2K):
        if ai & 1:
            count_bit[i] += 1
        ai = ai >> 1
b = 2**(log2K)
ans = 0
k_sum = 0
for i in range(log2K-1, -1, -1):
    if K >> i & 1:
        tmp = k_sum
        b = 1
        for j in range(i):
            tmp += max(count_bit[j], N-count_bit[j]) * b
            b *= 2
        tmp += count_bit[i] * b
        ans = max(tmp, ans)
        k_sum += (N-count_bit[i]) * b
    else:
        k_sum += count_bit[i] * (2**i)
ans = max(k_sum, ans)
print(ans)