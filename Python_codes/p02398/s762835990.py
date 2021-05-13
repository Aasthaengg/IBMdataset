a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)
j = 0
for i in range(b - a + 1):
    if c % (i + a) == 0:
        j += 1

print(j)