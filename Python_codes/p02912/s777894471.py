import heapq
import sys

def input():
    return sys.stdin.readline().strip()

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A = list(map(lambda x: x*(-1),A))

    heapq.heapify(A)

    for _ in range(M):
        max_value = heapq.heappop(A) * (-1)
        heapq.heappush(A,max_value//2 * (-1))

    print(sum(A) * (-1))

if __name__ == "__main__":
    main()