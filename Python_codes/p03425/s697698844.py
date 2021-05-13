import numpy,itertools
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
c = [0] * 5
for _ in range(n):
    s = readline().decode().rstrip()
    if s[0] == 'M':
        c[0] += 1
    elif s[0] == 'A':
        c[1] += 1
    elif s[0] == 'R':
        c[2] += 1
    elif s[0] == 'C':
        c[3] += 1
    elif s[0] == 'H':
        c[4] += 1

cm = list(itertools.combinations(c, 3))
arr = numpy.array(cm)

print(sum(list(numpy.prod(arr, axis=1))))