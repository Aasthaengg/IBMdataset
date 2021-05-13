t1, t2 = map(int,input().split())
a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())
a1 *= t1
b1 *= t1
a2 *= t2
b2 *= t2

if a1 + a2 == b1 + b2:
    print("infinity")
    exit()
if (a1 < b1 and a1+a2 < b1+b2) or (b1 < a1 and b1+b2 < a1+a2):
    print(0)
    exit()

d2 = abs(a1+a2-b1-b2)
d1 = abs(a1-b1)
print(1 + 2*(d1//d2) - (d1 % d2 == 0))