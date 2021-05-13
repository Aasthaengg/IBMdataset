import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from operator import itemgetter  
from collections import defaultdict
def main():
    n, m = map(int, readline().split())
    cities = []
    for i in range(m):
        p, y = map(int, readline().split())
        cities.append((i+1, p, y))
    cities.sort(key=itemgetter(2))
    dd = defaultdict(int)
    ansdd = defaultdict(str)
    for i in range(m):
        cid, p, y = cities[i]
        dd[p] += 1
        x = dd[p]
        ansdd[cid] = '{:0=6}'.format(p)+'{:0=6}'.format(x)
    for i in range(1, m+1):
        print(ansdd[i])
if __name__ == '__main__':
    main()
