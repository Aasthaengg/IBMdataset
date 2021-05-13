import sys

read = sys.stdin.read

ab = list(map(int, read().split()))

for i in (1, 2, 3, 4):
    if ab.count(i) > 2:
        print('NO')
        exit()
else:
    print('YES')
