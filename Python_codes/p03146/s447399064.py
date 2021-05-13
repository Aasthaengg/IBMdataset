s = int(input())
n = s
a = [0]*1000001
a[n] = 1
i = 1
while True:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    if a[n] == 1:
        ans = i + 1
        break
    a[n] = 1
    i += 1

print(ans)
