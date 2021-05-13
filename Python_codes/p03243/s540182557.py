n = int(input())

while True:
    a, b, c = str(n)
    if a == b and b == c:
        print(a+b+c)
        exit()
    else:
        n += 1