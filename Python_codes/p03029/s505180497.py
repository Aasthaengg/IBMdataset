a, p = map(int, input().split())

app = 3*a + p
pie = 0

while app >= 2:
    app -= 2
    pie += 1

print(pie)