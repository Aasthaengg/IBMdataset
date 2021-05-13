import sys
import math
readline = sys.stdin.readline

K = int(readline())
A = reversed(list(map(int, readline().split())))

a_min = 2
a_max = 2
for a in A:
    a_min = math.ceil(a_min / a) * a
    a_max = a * (a_max // a) + a - 1
    if a_min > a_max:
        print(-1)
        exit()
print('{} {}'.format(str(a_min), str(a_max)))
