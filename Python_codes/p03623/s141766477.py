x,a,b = map(int, input().split())
a = x - a
b = x - b

if a < 0:
    a = a * -1
if b < 0:
    b = b * -1

if a < b:
    print("A")
else:
    print("B")