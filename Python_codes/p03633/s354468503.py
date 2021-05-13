import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


N = int(input())
t_li = []
for _ in range(N):
    t_li.append(int(input()))
if N > 1:
    ans = lcm(t_li[0], t_li[1])
    for i in range(2, N):
        ans = lcm(ans, t_li[i])
else:
    ans = t_li[0]
print(ans)
