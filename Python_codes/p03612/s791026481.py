import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    P = [0] + list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if i == P[i]:
            P[i + 1] = P[i]
            ans += 1
    if N == P[N]: ans += 1
    print(ans)



if __name__ == "__main__":
    main()
