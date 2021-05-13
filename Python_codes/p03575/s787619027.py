from collections import deque


N, M = map(int, input().split())
to = [[] for _ in range(N)]
bridge = []

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    to[a].append(b)
    to[b].append(a)
    bridge.append(set([a, b]))


def main():
    ans = 0

    for b in bridge:
        seen = [0] * N
        seen[0] = 1
        
        # BFS
        que = deque([0])
        while que:
            v = que.popleft()
            for nv in to[v]:
                if set([v, nv]) == b:
                    continue
                if not seen[nv]:
                    seen[nv] = 1
                    que.append(nv)

        if seen != [1] * N:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()