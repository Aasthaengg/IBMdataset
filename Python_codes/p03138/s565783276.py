import sys
import math
N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
bin_k = bin(K)[2:].zfill(50)
cnt = [0] * 50

for a in A:
    bin_a = bin(a)[2:]
    for i, b in enumerate(bin_a[::-1]):
        if b == "1":
            cnt[i] += 1

cnt = cnt[::-1]

ans = 0
base = 2**(50 - 1)
flag = False
for i, c in enumerate(cnt):
    if flag:
        ans += base * max(c, N - c)
    else:
        if bin_k[i] == "1":
            if c >= N - c:
                ans += base * c
                flag = True
            else:
                ans += base * (N - c)

        else:
            ans += base * c
    base //= 2
print(ans)