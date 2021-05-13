import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    N, W = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(N)]

    d = defaultdict(lambda: 0)
    q = deque()
    for a in A:
        while len(q) > 0:
            w0, v0 = q.popleft()

            w1 = w0 + a[0]
            v1 = v0 + a[1]

            if w1 <= W:
                d[w1] = max(d[w1], v1)

            d[w0] = max(d[w0], v0)

        if a[0] <= W:
            q.append(a)

        for key in d.keys():
            q.append((key, d[key]))

    ans = 0
    for key in d.keys():
        ans = max(ans, d[key])

    return ans


if __name__ == '__main__':
    print(main())
