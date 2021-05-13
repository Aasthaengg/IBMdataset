a = int(input())
ar = []
for i in range(a):
    l = list(map(int,input().split(" ")))
    ar.append(l)
ar.reverse()
count = 0
for r in ar:
    x = r[0] + count
    y = r[1]
    m = x % y
    if m != 0:
        count += y - m
print(count)