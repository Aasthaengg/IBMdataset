import math
n, m = map(int, input().split())

if n == 1:
    print(m)
    exit()
a = []
b = []
for i in range(1, math.ceil(math.sqrt(m))):
    if m % n == 0:
        print(m // n)
        exit()
    if m % i == 0:
        b.append(i)
        b.append(m // i)
        
#print(b)

for i in range(len(b)):
    if b[i] * n <= m:
        a.append(b[i])
#print(a)

if len(b) == 2:
    print(1)
else:
    print(max(a))
