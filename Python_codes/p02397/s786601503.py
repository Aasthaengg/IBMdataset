i = 0
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        i = a; a = b; b = i
    print("{} {}".format(a, b))
