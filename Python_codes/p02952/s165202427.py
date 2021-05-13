import math

N = int(input())

ans = 0

for i in range(int(math.log10(N)) + 1):
    if i % 2 != 0:
        pass
    elif i == int(math.log10(N)):
        ans += N - 10**i + 1
    else:
        ans += 10**(i+1) - 10**i

print(ans)