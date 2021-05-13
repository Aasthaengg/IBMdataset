def gcd(a, b):
    while b != 0:
        y = a % b
        a = b
        b = y
    return a


d = []
m = []
while True:
    try:
        a, b = map(int, input().split())
        if a > b:
            num = gcd(a, b)
        elif a < b:
            num = gcd(b, a)
        else:
            num = a
        d.append(num)
        m.append(int(a*b/num))
    except EOFError:
        break

for i in range(len(d)):
    print(d[i], m[i])