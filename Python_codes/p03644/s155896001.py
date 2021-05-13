n = int(input())
a = 1
while True:
    a *= 2
    if n < a:
        print(int(a / 2))
        break