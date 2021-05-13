h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(h)]

ansl = []
n = 0
for i in range(h):
    for j in range(w-1):
        if a[i][j] % 2 == 0:
            pass
        else:
            n += 1
            ansl.append([i+1, j+1, i+1, j+2])
            a[i][j] -= 1
            a[i][j+1] += 1

for i in range(h-1):
    if a[i][w-1] % 2 == 0:
        pass
    else:
        n += 1
        ansl.append([i+1, w, i+2, w])
        a[i][w-1] -= 1
        a[i+1][w-1] += 1

print(n)
[print(*x) for x in ansl]
