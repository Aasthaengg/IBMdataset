import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import accumulate
from itertools import chain
from collections import deque
def main():
    n = int(input())
    a1 = chain(tuple([0]), tuple(map(int, input().split())))
    a2 = chain(tuple([0]), tuple(map(int, input().split())))

    a1a = tuple(accumulate(a1))
    a2a = tuple(accumulate(a2))
    scores = deque()
    for i1 in range(1, n + 1):
        scores.append(a1a[i1] + a2a[n] - a2a[i1 - 1])
    r = max(scores)
    print(r)
if __name__ == '__main__':
    main()
