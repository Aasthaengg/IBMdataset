n, m = map(int, input().split())
a = sorted([int(i) for i in input().split()])
bc = sorted([tuple(map(int, input().split())) for i in range(m)], key=lambda x: x[1], reverse=True)
i = 0
for b, c in bc:
    while b:
        if i < n and a[i] < c:
            a[i] = c
            b -= 1
        else:
            break
        i += 1
print(sum(a))