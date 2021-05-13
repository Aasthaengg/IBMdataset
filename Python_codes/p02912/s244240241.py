import heapq

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N, M = mi()
    A = list(map(lambda x: -int(x), input().split()))
    heapq.heapify(A)
    for i in range(M):
        t = heapq.heappop(A)
        heapq.heappush(A, -(-t//2))
    print(-sum(A))

if __name__ == '__main__':
    main()
