n = int(input())
x = [int (z) for z in input().split(' ')]
tn = n - 1
for c in range(0,n):
    print("%d" % x[tn], end='')
    if c != n-1:
        print(' ', end='')
    tn -= 1
print('')