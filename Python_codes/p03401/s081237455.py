n = int(input())
a = [0] + list(map(int, input().split())) + [0]
money = 0
now = 0
for i in a:
    money += abs(now - i)
    now = i


for i in range(1, n+1):
    if a[i-1] <= a[i+1]:
        if a[i - 1] <= a[i] <= a[i + 1]:
            print(money)
        elif a[i] < a[i - 1]:
            print(money - 2 * (a[i - 1] - a[i]))
        elif a[i + 1] < a[i]:
            print(money - 2 * (a[i] - a[i + 1]))
    else:
        if a[i + 1] <= a[i] <= a[i - 1]:
            print(money)
        elif a[i] < a[i + 1]:
            print(money - 2 * (a[i + 1] - a[i]))
        elif a[i - 1] < a[i]:
            print(money - 2 * (a[i] - a[i - 1]))


