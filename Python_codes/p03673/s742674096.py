n = int(input())
a = input().split()
reb_a = a[::-1]
if n % 2 == 0:
    res = reb_a[::2]+a[::2]
else:
    res = reb_a[::2]+a[1::2]

print(' '.join(res))