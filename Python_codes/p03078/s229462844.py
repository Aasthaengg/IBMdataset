import sys
import heapq


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    Q = []
    S = set()
    heapq.heapify(Q)
    heapq.heappush(Q, (-A[0] - B[0] - C[0], 0, 0, 0))
    for i in range(K):
        m, a, b, c = heapq.heappop(Q)
        print(-m)
        if (a + 1, b, c) not in S and a + 1 < X:
            heapq.heappush(Q, (-A[a + 1] - B[b] - C[c], a + 1, b, c))
            S.add((a + 1, b, c))
        if (a, b + 1, c) not in S and b + 1 < Y:
            heapq.heappush(Q, (-A[a] - B[b + 1] - C[c], a, b + 1, c))
            S.add((a, b + 1, c))
        if (a, b, c + 1) not in S and c + 1 < Z:
            heapq.heappush(Q, (-A[a ] - B[b] - C[c+1], a, b, c + 1))
            S.add((a, b, c + 1))


if __name__ == "__main__":
    main()
