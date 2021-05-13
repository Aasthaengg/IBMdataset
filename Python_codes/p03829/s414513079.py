import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()


def main():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))
    ans = 0
    now = X[0]
    for i in range(1, N):
        ans += min(B, A * (X[i] - now))
        now = X[i]
    print(ans)




if __name__ == "__main__":
    main()
