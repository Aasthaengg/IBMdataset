from heapq import heappop, heapify, heappush
def main():
    n, m = list(map(int, input().split()))
    A = list(map(lambda x: -int(x), input().split()))
    heapify(A)
    for _ in range(m):
        a = heappop(A)
        if a == 0:
            break
        a = -int(-a // 2)
        heappush(A, a)
    print(sum([-a for a in A]))

if __name__ == '__main__':
    main()
