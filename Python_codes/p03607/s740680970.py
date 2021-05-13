n = int(input())
d = {}
for _ in range(n):
    a = int(input())
    if a in d:
        del d[a]
    else:
        d[a] = 1
print (len(d))
