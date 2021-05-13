import math
import collections
import fractions
import itertools

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    deq = collections.deque()
    for i in range(n):
        if i % 2 == 0:
            deq.append(str(a[i]))
        else:
            deq.appendleft(str(a[i]))
    if n % 2 == 1:
        deq.reverse()
    print(" ".join(deq))
    return 0

if __name__ == "__main__":
    solve()
