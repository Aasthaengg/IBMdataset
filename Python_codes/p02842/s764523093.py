import math

n = int(input())
ans = -1

for i in range(1, n+1):
    if math.floor(i * 1.08) == n:
        ans = i

if ans != -1:
    print(ans)
else:
    print(":(")
