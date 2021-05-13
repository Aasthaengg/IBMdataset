from heapq import heappop, heappush
def main():
    def push(i, j, k):
        nonlocal A, B, C, ADD
        if i >= x or j >= y or k >= z: return
        if (i, j, k) not in ADD:
            heappush(H, (A[i] + B[j] + C[k], i, j, k))
            ADD.add((i, j, k))
    x, y, z, k = map(int, input().split())
    INF = 10 ** 11
    A = sorted(list(map(lambda x: -int(x), input().split())))
    B = sorted(list(map(lambda x: -int(x), input().split())))
    C = sorted(list(map(lambda x: -int(x), input().split())))
    H = []
    ADD = set()
    push(0, 0, 0)
    for _ in range(k):
        ans, i, j, k = heappop(H)
        push(i + 1, j, k)
        push(i, j + 1, k)
        push(i, j, k + 1)
        print(-ans)

if __name__ == '__main__':
    main()
