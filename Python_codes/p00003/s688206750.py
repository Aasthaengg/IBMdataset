import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    line = sys.stdin.readline()
    lengths = sorted(list(map(int, line.strip().split())))
    if lengths[0]**2 + lengths[1]**2 == lengths[2]**2:
        print('YES')
    else:
        print('NO')