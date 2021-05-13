N = int(input())
A = list(map(int, input().split()))
abs_min = 10 ** 9
minus = 0
total = 0
for x in A:
    if x < 0:
        minus += 1
        x = - x
    if abs_min > x:
        abs_min = x
    total += x
if minus % 2 == 0:
    print(total)
else:
    print(total - abs_min * 2)