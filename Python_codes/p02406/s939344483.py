n = int(input())
a = []

for i in range(1, n+1):
    if i % 3 == 0 or '3' in str(i):
        print(' %d' % i, end='')
print('')