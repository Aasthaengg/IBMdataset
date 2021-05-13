import sys
from operator import itemgetter
read = sys.stdin.read

N, *P = map(int, read().split())
p = sorted(enumerate(P), key=itemgetter(1))

length = []
cnt = 1
for i in range(N - 1):
    if p[i + 1][0] < p[i][0]:
        length.append(cnt)
        cnt = 1
    else:
        cnt += 1

length.append(cnt)

print(N - max(length))