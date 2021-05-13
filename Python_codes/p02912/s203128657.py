import heapq

def main():
    N, M = map(int, input().split())
    A = [-v for v in list(map(int, input().split()))]
    heapq.heapify(A)
    for _ in range(M):
        v = heapq.heappop(A)
        heapq.heappush(A, v / 2)
    print(sum([int(-v) for v in A]))


if __name__ == '__main__':
    main()
