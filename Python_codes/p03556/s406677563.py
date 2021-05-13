import math

n = int(input())
i = n

while True:
    x = int(math.sqrt(i))
    if x ** 2 == i:
        ans = i
        break
    i -= 1
print(ans)