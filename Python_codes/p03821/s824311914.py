import math

N = int(input())
a_li = []
b_li = []
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    a_li.append(a)
    b_li.append(b)
for i in reversed(range(N)):
    a, b = a_li[i], b_li[i]
    a += ans
    div = math.ceil(a / b)
    ans += b * div - a
print(ans)
