a = int(input())
b = int(input())
c = int(input())
d = int(input())
money = 0
if a <= b:
    money += a
elif b < a:
    money += b
if c <= d:
    money += c
elif d < c:
    money += d
print(money)