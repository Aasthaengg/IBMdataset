t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

a = (a1-b1)*t1
b = (a2-b2)*t2
if a < 0:
    a *= -1
    b *= -1

if a == -b:
    print("infinity")
    exit()
if a+b > 0:
    print(0)
else:
    c = -a-b
    print((a+c-1)//c + a//c)
