import math

n, c, k =map(int, input().split())
t = list(int(input()) for _ in range(n))

t.sort()

ans = 0
tm = 0
passenger = 0

for i in range(n):
    if passenger == 0 or t[i] > tm + k or passenger == c:
        tm = t[i]
        passenger = 1
        ans += 1
    else:
        passenger += 1

print(ans)
