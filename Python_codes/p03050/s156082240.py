N = int(input())
import math

ans = 0
for Q in range(1, math.floor(math.sqrt(N)) + 1):
    if N % Q == 0:
        if Q <= N // Q - 2:
            ans += N // Q - 1
            # print(k - 1)
print(ans)