from collections import deque


def main():

    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    q = deque()
    score = [0] * N
    seen = [0] * N
    for _ in range(Q):
        a, s = map(int, input().split())
        score[a-1] += s

    q.append(0)
    while q:
        tmp = q.pop()
        seen[tmp] += 1
        for v in G[tmp]:
            if seen[v]:
                continue
            q.append(v)
            score[v] += score[tmp]

    print(*score)


if __name__ == '__main__':
    main()
