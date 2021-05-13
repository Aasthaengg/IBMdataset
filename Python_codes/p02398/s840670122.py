l = map(int, raw_input().split())
a = l[0]
b = l[1]
c = l[2]
k = 0
for n in range(a, b+1):
    if c % n == 0:
        k = k + 1
print k