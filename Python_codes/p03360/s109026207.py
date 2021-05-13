import sys
import heapq

def main():
    A, B, C = map(int, input().split())
    K = int(input())

    heap = [-A, -B, -C]
    heapq.heapify(heap)
    for _ in range(K):
        max = heapq.heappop(heap)
        heapq.heappush(heap, max * 2)
    
    sum = 0
    for i in heap:
        sum += i
    print(-sum)

if __name__ == '__main__':
    main()
