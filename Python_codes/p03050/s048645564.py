import math
N = int(input())
ans = 0
for i in range(1,math.ceil(N**0.5)):
    a = N - i
    if a % i == 0 and a/i >0 and a/i>i:
        ans += a/i
print(int(ans))