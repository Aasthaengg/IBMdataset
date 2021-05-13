N, Y = map(int, input().split())

a = -1
b = -1
c = -1
judge = False

for x in range(N, -1, -1):
    money_max = x * 10000 + (N-x) * 5000
    money_min = x * 10000 + (N-x) * 1000
    if money_min <= Y and Y <= money_max:
        for y in range(N-x, -1, -1):
            money = x * 10000 + y * 5000 + (N - x - y)* 1000
            if money == Y:
                a = x
                b = y
                c = N - (x + y)
                judge = True
                break
    if judge:
        break
print(a, b, c)