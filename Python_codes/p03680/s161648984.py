n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

c = 0
i = 0
while True:
    i = a[i]  - 1
    c += 1
    if i == 1:
        print(c)
        break
    if c > n:
        print(-1)
        break