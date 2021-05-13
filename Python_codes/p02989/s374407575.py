import sys
N = int(input())
d = list(map(int, input().split()))
if len(d) % 2 != 0:
    print(0)
    sys.exit()
d.sort()
if d[N//2] == d[N//2-1]:
    print(0)
else:
    print(d[N//2] - d[N//2-1])
