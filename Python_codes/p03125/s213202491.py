a = int()
b = int()

1 <= a <= b <=20

a,b=(int(x) for x in input().split())


if b % a == 0:
    print(a + b)
else :
    print(b - a)
