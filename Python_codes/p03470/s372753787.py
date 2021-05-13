n = int(input())
a = list(int(input()) for i in range(n))

a.sort()
count = 0

for i, j in enumerate(a):
    try:
        if j == a[i + 1]:
            a[i] = 0
            count += 1
        else:
            pass
    except IndexError:
        pass

print(n - count)
