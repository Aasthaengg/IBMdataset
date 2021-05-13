num = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
first = second = third = inf = 0.00000
for i in range(num):
    dif = x[i] - y[i]
    first = first + abs(dif)
    second = second + dif ** 2
    third = third + abs(dif) ** 3
    inf = max(inf, abs(dif))
print('{:.6f}'.format(first))
print('{:.6f}'.format(second ** 0.5))
print('{:.6f}'.format(third ** 0.333333333333333333))
print('{:.6f}'.format(inf))
