from math import ceil
a, b = map(int, input().split())
b -= 1
ans = ceil(b / (a - 1))
print(ans)
