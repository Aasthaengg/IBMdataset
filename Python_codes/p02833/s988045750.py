import sys

N = int(input())
# 5^26 > 10^18
if N % 2 == 1:
    print(0)
    sys.exit()

ans = 0
mul = 1
for i in range(1, 27):
    mul *= 5
    add = N // (2 * mul)
    if add == 0: break
    ans += add

print(ans)