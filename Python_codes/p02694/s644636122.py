x = int(input())
c = 100
i = 0

while True:
    c += c // 100
    i += 1
    if c >= x:
        print(i)
        break