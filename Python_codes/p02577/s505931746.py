import sys

a = sum([int(num) for num in list(input())]) % 9

if a == 0:
    print('Yes')
else:
    print('No')