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
X = 0
for c in count_bit[::-1]:
    b //= 2
    if c*2 < N and X + b <= K:
        X += b
ans = 0
for ai in A:
    ans += X ^ ai
print(ans)