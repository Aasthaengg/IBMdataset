from math import sqrt
n = int(input())
end = int(sqrt(n))
low = 1

for x in range(end, 0, -1):
    if n % x == 0:
        low = x
        break

high = int(n/low)
ans = low + high -2
print(ans)