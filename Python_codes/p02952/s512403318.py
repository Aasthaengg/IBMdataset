import math
n = int(input())
ans = 0
for i in range(1,n+1):
    if int(math.log10(i)) % 2 == 0:
        ans += 1
print(ans)