n = int(input())
for i in range(3, n+1):
    if i % 3 == 0:
        print(' {}'.format(i), end='')
        continue
    if '3' in str(i):
        print(' {}'.format(i), end='')
        continue
print()