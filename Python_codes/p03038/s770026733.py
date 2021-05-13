def main():
    from heapq import heapify, heappushpop
    _, M = (int(i) for i in input().split())
    A = ([int(i) for i in input().split()])
    BC = [[int(i) for i in input().split()] for j in range(M)]

    heapify(A)
    BC.sort(lambda p: p[1], reverse=True)
    for b, c in BC:
        if A[0] >= c:
            break
        for _ in range(b):
            if A[0] >= c:
                break
            heappushpop(A, c)
    print(sum(A))


if __name__ == '__main__':
    main()
