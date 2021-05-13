import numpy as np
n, k = map(int, input().split())
a = np.array(list(map(int, input().split())))

one = np.zeros(40, dtype=int)
for i in range(40):
    one[i] = np.count_nonzero(a % 2)
    a >>= 1
zero = n-one

bk = bin(k)[2:].zfill(40)
bk = bk[::-1]
answer = 0
tmp = 0
for i in range(40 - 1, -1, -1):
    if bk[i] == "0":
        tmp += one[i] * (2 ** i)
    else:
        ans = tmp + one[i] * (2 ** i)
        for j in range(i - 1, -1, -1):
            ans += max(one[j], zero[j]) * (2 ** j)
        answer = max(answer, ans)
        tmp += zero[i] * (2 ** i)
else:
    answer = max(answer, tmp)

print(answer)
