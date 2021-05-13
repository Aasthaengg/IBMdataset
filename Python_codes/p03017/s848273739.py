import sys

n, a, b, c, d = map(int, input().split())
a, b, c, d = a - 1, b - 1, c - 1, d - 1
s = input()

for i in range(a + 1, max(c, d) - 1):
    if s[i: i + 2] == '##':
        print('No')
        sys.exit()

if c < d:
    print('Yes')
    sys.exit()

for i in range(b, d + 1):
        if s[i - 1: i + 2] == '...':
            print('Yes')
            sys.exit()

print('No')