n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
b = 0
bi = 0
c = 0
for i in range(n - 1):
    if a[i] == a[i + 1]:
        b = a[i]
        bi = i + 1
        break
if bi != 0:
    for i in range(bi + 1, n - 1):
        if a[i] == a[i + 1]:
            c = a[i]
            break
print(b * c)