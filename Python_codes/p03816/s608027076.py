from collections import Counter
n = int(input())
list_A = list(map(int, input().split()))
l = Counter(list_A)

list_B = l.values()

value_1 = 0
value_2 = 0
value_0 = 0

for num in list_B:
    a = num
    while True:
        a = a % 3 + a // 3
        if a < 3:
            break
    if a == 2:
        value_2 += 1
    elif a == 1:
        value_1 += 1
    else:
        value_0 += 1

ans = value_1 + 2*(value_2//2) + value_0

print(ans)