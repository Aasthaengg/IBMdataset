n = int(input())
a = []
b = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

tot = 0
for i in range(n)[::-1]:
    a[i] += tot
    # print(i, a[i])
    if a[i] != 0:
        if a[i] % b[i] == 0:
            continue
        else:
            tot += b[i]*(a[i]//b[i] + 1) - a[i]
    else:
        tot += a[i]
    # print(tot)
print(tot)