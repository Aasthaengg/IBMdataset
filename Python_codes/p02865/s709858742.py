import sys

n = int(input())

if n % 2 == 0:
    ans = int(n / 2) - 1
else:
    ans = int(n / 2)

print('{}'.format(ans))