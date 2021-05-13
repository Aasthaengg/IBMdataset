a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
orders = sorted([a, b, c, d, e], key=lambda x: 10 if x % 10 == 0 else x % 10, reverse=True)
total = 0
for o in orders[:-1]:
    total += ((o + 9) // 10) * 10
total += orders[-1]
print(total)
