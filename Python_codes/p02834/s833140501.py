from collections import deque


def main():
    N, u, v = map(int, input().split())
    adj = [set() for _ in range(N)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        adj[A-1].add(B-1)
        adj[B-1].add(A-1)
    move = [-1] * N
    q = deque([(v-1, 0)])
    while len(q):
        cur, c = q.popleft()
        move[cur] = c
        for nxt in adj[cur]:
            if move[nxt] == -1:
                q.append((nxt, c+1))
    reachable = [False] * N
    q = deque([(u-1, 0)])
    while len(q):
        cur, c = q.popleft()
        reachable[cur] = True
        for nxt in adj[cur]:
            if c+1 <= move[nxt] and not reachable[nxt]:
                q.append((nxt, c+1))
    ans = 0
    for i in range(N):
        if reachable[i] and len(adj[i]) >= 2:
            ans = max(ans, move[i])
    print(ans)


if __name__ == "__main__":
    main()
