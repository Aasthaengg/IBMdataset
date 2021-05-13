n, k = input().split(' ')
n, k = int(n), int(k)
maxval = 1
if k == 1:
    print(0)
else:
    while n - maxval - k + 1 != 0:
        maxval += 1
    print(maxval - 1)