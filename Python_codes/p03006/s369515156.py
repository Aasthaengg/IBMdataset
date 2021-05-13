import itertools
import collections

N = int(input())
x_y = [list(map(int, input().split())) for _ in range(N)]

count = collections.defaultdict(int)
for i in itertools.combinations(x_y, 2):
    count[(i[0][0]-i[1][0], i[0][1]-i[1][1])] += 1
    count[(i[1][0]-i[0][0], i[1][1]-i[0][1])] += 1
if not count:
    print(N)
else:
    print(N-max(count.values()))