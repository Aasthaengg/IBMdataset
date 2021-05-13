from collections import deque


def main():
    n, m = map(int, input().split())
    is_checked = [False for _ in range(n+1)]
    edges = [[] for _ in range(n+1)]
    ans = 0

    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    for ni in range(n):
        if is_checked[ni]:
            continue
        is_checked[ni] = True
        q = deque([ni])
        depth = 0
        while len(q) > 0:
            p = q.popleft()
            for e in edges[p]:
                if not is_checked[e]:
                    is_checked[e] = True
                    q.append(e)
            depth += 1

        ans = max(ans, depth)

    print(ans)


if __name__ == '__main__':
    main()
