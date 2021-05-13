from heapq import heappop, heappush, heapify
def main():
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(m)]
    heapify(A)
    B.sort(key = lambda x: x[1], reverse = True)
    for (b, c) in B:
        if c > A[0]:
            for i in range(b):
                a = heappop(A)
                heappush(A, max(a, c))
    print(sum(A))


if __name__ == '__main__':
    main()
