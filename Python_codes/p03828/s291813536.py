import numpy as np
MOD = 1000000007
n = int(input())

cnt = np.ones(n+1)

for i in range(2, n+1):
    m = i
    for j in range(2, i+1):
        while m % j == 0:
            m = m / j
            cnt[j] += 1
ans = 1
for i in range(2, n+1):
    ans = (ans * cnt[i]) % MOD
print(int(ans))