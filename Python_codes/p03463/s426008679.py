import sys
n, a, b = map(int, input().split())
if (b - a) % 2 == 1:
    ans = "Borys"
else:
    ans = "Alice"
print(ans)
