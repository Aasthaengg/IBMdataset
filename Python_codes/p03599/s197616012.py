A,B,C,D,E,F = map(int,input().split())

water = set()
sugar = set()

s = 0
a = 0
b = 0

for i in range(30):
    for j in range(30-i):
        if 100*A*i+100*B*j <= F:
            water.add(100*A*i+100*B*j)

water.remove(0)

for i in range(3000):
    for j in range(3000-i):
        if C*i+D*j <= F:
            sugar.add(C*i+D*j)

sugar.remove(0)

WATER = list(water)
SUGAR = list(sugar)

for i in WATER:
    for j in SUGAR:
        if (j <= i*E/100) and (i+j <= F):
            if s == 0:
                s = 100*j /(i + j)
                a = i
                b = j
            else:
                if s < 100*j /(i + j):
                    s = 100*j /(i + j)
                    a = i
                    b = j

if a == 0 and b == 0:
    print(100*A,0)
else:
    print(a+b,b)
