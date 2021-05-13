L = raw_input().split()
a = int(L[0])
b = int(L[1])
c = int(L[2])
i = 0
for x in range(a, b+1):
    if c % x == 0:
        i = i + 1

print i