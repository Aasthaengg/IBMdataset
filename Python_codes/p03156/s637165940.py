n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
c, d, e = 0, 0, 0
for pp in p:
    if pp <= a:
        c += 1
    elif pp <= b:
        d += 1
    else:
        e += 1
print(min(c, d, e))
