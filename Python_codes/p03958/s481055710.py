import sys
import heapq

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    K, T = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    h = []
    for i in range(T):
        heapq.heappush(h, (-A[i], i))

    ans = 0
    p = -1

    while h:
        c = heapq.heappop(h)
        if p == c[1]:
            if h:
                c2 = heapq.heappop(h)
                heapq.heappush(h, c)
                x = c2[0]
                y = c2[1]
                p = y
                x += 1
                if x != 0:
                    heapq.heappush(h, (x, y))
            else:
                ans = c[0]
                break
        else:
            x = c[0]
            y = c[1]
            x += 1
            p = y
            if x != 0:
                heapq.heappush(h, (x, y))

    print(-ans)


if __name__ == '__main__':
    main()
