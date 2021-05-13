x = int(input())
y = [int(i) for i in input().split()]
print("{0}".format(y[-1]),end='')
for i in range(x-2, 0-1, -1):
    print(' {0}'.format(y[i]), end='')
print()