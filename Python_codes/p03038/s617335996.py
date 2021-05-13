from operator import itemgetter

n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = [tuple(int(i) for i in input().split()) for _ in range(m)]

a.sort()
bc.sort(key=itemgetter(1), reverse=True)
idx = 0
b, c = bc[idx]
for i in range(n):
    if a[i] >= c:
        break
    a[i] = c
    b -= 1

    if b == 0:
        idx += 1
        if idx >= m:
            break
        b, c = bc[idx]

print(sum(a))
