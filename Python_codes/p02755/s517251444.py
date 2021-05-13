a, b = map(int, input().split())

x = 1
while x <= 1100:
    if (x*8//100) == a and (x//10) == b:
        print(x)
        break
    x += 1
else:
    print(-1)