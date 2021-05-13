temp = []
l = []
a, b, k = map(int, input().split())

for i in range(1, a + 1):
    if a % i == 0:
        temp.append(i)

for i in range(1, b + 1):
    if b % i == 0 and i in temp:
        l.append(i)

print(l[k * -1])