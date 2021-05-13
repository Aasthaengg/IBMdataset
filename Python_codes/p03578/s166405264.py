import math
import collections
import fractions
import itertools

def solve():
    n = int(input())
    d = list(map(int, input().split()))
    m = int(input())
    t = list(map(int, input().split()))
    t = collections.Counter(t)
    d = collections.Counter(d)
    for i in t:
        if t[i] > d[i]:
            print("NO")
            break
    else:
        print("YES")
    return 0

if __name__ == "__main__":
    solve()