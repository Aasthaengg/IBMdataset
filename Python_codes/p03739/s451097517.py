def f(c, cost):
    for i in a[1:]:
        if c > 0:
            if c + i >= 0:
                cost += c + i + 1
                c = -1
            else:
                c += i
        else:
            if c + i <= 0:
                cost += 1 - c - i
                c = 1
            else:
                c += i
    return c, cost


n = int(input())
a = list(map(int, input().split()))
cost = (a[0] == 0)
c = a[0] + (a[0] == 0)
c, cost = f(c, cost)
tmp = cost
cost = 0
if a[0] >= 0:
    cost = a[0] + 1
    c = -1
else:
    cost = -a[0] + 1
    c = 1
c, cost = f(c, cost)
print(int(min(cost, tmp)))
