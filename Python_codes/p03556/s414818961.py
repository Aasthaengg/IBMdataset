import math
N = int(input())
ans = 1
for i in range(10**5):
    if i**2 <= N:
        ans = i**2
    if i**2 > N:
        break

print(ans)
