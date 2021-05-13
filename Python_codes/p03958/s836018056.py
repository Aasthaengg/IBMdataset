from heapq import heappush, heappop, heapify
def main():
    k, t = map(int, input().split())
    A = list(map(lambda x: -int(x), input().split()))
    heapify(A)
    tmp = heappop(A)
    while A:
        now = heappop(A)
        if tmp != -1:
            heappush(A, tmp + 1)
        tmp = now
    print(-(tmp + 1))

if __name__ == '__main__':
    main()
