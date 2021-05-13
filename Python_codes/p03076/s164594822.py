a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

menu = [a, b, c, d, e]

mintime = 9
minindex = 4
for i, m in enumerate(menu):
    if m % 10 == 0:
        continue

    if m % 10 < mintime:
        minindex = i
        mintime = m % 10

ans = menu[minindex]
for i, m in enumerate(menu):
    if i == minindex:
        continue
    if m % 10 != 0:
        m += 10 - m % 10
    ans += m

print(ans)
