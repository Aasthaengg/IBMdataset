n, k = map(int, input().split())
a = list(map(int, input().split()))


fi = 0
for i in range(n):
    if a[i] == 1:
        fi = i
        break

if (n - 1) % (k - 1) == 0:
    print((n - 1) // (k - 1))
else:
    print((n - 1) // (k - 1) + 1)
