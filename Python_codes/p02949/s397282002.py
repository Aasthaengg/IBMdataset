n, m, p = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]


def bellman_ford(s, g):
    # loop 0 - (n-1) : bellman ford
    # loop n - (2n-1): check g can be updated
    dist = [float("inf")] * n
    dist[s] = 0
    for i in range(2 * n):
        for a, b, c in abc:
            a -= 1
            b -= 1
            cost = -(c - p)

            if dist[b] > dist[a] + cost:
                dist[b] = dist[a] + cost
                if i >= n:
                    dist[b] = -float("inf")

    if dist[g] == -float("inf"):
        return -1

    else:
        return max(-dist[g], 0)


ans = bellman_ford(0, n - 1)
print(ans)
