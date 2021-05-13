paints = input().split()

a = int(paints[0])
b = int(paints[1])
c = int(paints[2])

if a == b == c:
    print(1)
elif a==b or b==c or c==a:
    print(2)
else:
    print(3)

