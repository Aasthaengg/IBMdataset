n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
d = [tuple(map(int, input().split())) for _ in range(m)]
d.sort(key=lambda p: -p[1])
now = 0
for b, c in d:
    while b > 0:
        if c > a[now]:
            a[now] = c
            now += 1
            b -= 1
            if now == len(a):
                break
        else:
            break
    if now == len(a):
        break
print(sum(a))
