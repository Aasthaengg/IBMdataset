import math
n = int(input())
ans = 1

for i in range(1,math.ceil(math.sqrt(n))):
    for j in range(2,11):
        if i ** j > n and j > 2:
            ans = max(ans,i ** (j-1))
            break

print(ans)