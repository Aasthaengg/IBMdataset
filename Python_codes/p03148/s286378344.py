import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))
from heapq import heappush, heappop

def main():
    n, k = map(int, input().split())
    td = [tuple(map(int, input().split())) for _ in range(n)]
    td = list(sorted(td, key=lambda x: -x[1]))
    dsum, kind = 0, 0
    num = [0 for _ in range(n)]
    h = []
    for t, d in td[:k]:
        dsum += d
        if num[t-1] > 0:
            heappush(h, (d, t))
        if num[t-1] == 0:
            kind += 1
        num[t-1] += 1
    
    ans = dsum + kind * kind

    for t, d in td[k:]:
        if len(h) == 0:
            break
        if num[t-1] > 0:
            continue
        else:
            _d, _t = heappop(h)
            num[_t-1] -= 1
            num[t-1] += 1
            kind += 1
            dsum += d-_d
            if dsum + kind * kind > ans:
                ans = dsum + kind * kind
    
    print(ans)


if __name__ == '__main__':
    main()
