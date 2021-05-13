n = int(input())
a = list(map(int, input().split()))

ans = 10 ** 18
for z in range(2):
    if z == 0:
        sign = 1
    else:
        sign = -1
    c = 0
    cost = 0
    for x in a:
        c += x
        if c * sign <= 0:
            cost += 1 - c * sign
            c = sign
        sign *= -1
    ans = min(ans, cost)
print(ans)