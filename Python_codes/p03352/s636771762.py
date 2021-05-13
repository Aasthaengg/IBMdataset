import math

X = int(input())

ans = 1
for b in range(int(math.sqrt(X)) + 1):
    for p in range(10):
        if b ** p <= X:
            ans = max(ans, b ** p)
        else:
            break

print(ans)