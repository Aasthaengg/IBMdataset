import sys
from sys import stdin

n = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().rstrip().split()))
tmp = a[0]
for i in range(1, len(a)):
    tmp = tmp ^ a[i]
for i in range(1, len(a)):
    if a[i] ^ tmp == a[i]:
        print('Yes')
        sys.exit()
print('No')