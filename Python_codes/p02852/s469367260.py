#!python3

from collections import deque

LI = lambda: list(map(int, input().split()))

# input
N, M = LI()
S = input()

INF = 10 ** 6


def main():
    w = [(INF, INF)] * (N + 1)
    w[0] = (0, 0)
    # (cost, index)
    dq = deque([(0, 0)])
    for i in range(1, N + 1):
        if i - dq[0][1] > M:
            dq.popleft()
        if len(dq) == 0:
            print(-1)
            return
        if S[i] == "0":
            w[i] = (dq[0][0] + 1, i - dq[0][1])
            dq.append((w[i][0], i))

    ans = []
    x = N
    while x > 0:
        d = w[x][1]
        ans.append(d) 
        x -= d
    ans = ans[::-1]
    print(*ans)


if __name__ == "__main__":
    main()
