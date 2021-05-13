x = int(input())

s = 0
i = 1
while True:
    s += i
    if s >= x:
        print(i)
        break
    i += 1