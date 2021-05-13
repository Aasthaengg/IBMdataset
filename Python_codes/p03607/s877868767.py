N = int(input())
a = [input() for _ in range(N)]
d = {}
for i in range(N):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d.pop(a[i])
print(len(d))
