
from heapq import *
def main():
    import sys;input=sys.stdin.readline
    N, Q = map(int, input().split())
    X = []
    for _ in range(N):
        s, t, x = map(int, input().split())
        X.append((2*s-2*x-1, 0, x))
        X.append((2*t-2*x-1, 1, x))
    inf = 10**18
    X.append((-inf, 0, inf))
    X.append((inf, 1, inf))
    X.sort(key=lambda x: x[0])

    j = 0
    ll = []
    vs = set()
    d = dict()
    for _ in range(Q):
        q = int(input())
        while 1:
            u, f, x = X[j]
            if u > 2*q:
                break
            if f:
                if x not in d:
                    d[x] = 0
                d[x] += 1
            else:
                heappush(ll, x)
            j += 1
        while 1:
            x = heappop(ll)
            if x in d and d[x] > 0:
                d[x] -= 1
                continue
            heappush(ll, x)
            if x == inf:
                print(-1)
            else:
                print(x)
            break

if __name__ == '__main__':
    main()
