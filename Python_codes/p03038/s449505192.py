import sys
import heapq


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    L = []
    heapq.heapify(L)
    for a in A:
        heapq.heappush(L, (-a, 1))

    for i in range(M):
        b, c = map(int, input().split())
        heapq.heappush(L, (-c, b))
    ans = 0
    count = 0
    while True:
        c, b = heapq.heappop(L)
        if count +b >=N:
            print(-ans - c*(N-count))
            exit()
        count += b
        ans +=b*c

if __name__ == "__main__":
    main()
