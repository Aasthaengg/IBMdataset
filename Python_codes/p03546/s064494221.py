import heapq


def min_mp_to_one(C):
    # calculate minimum magical power to change number to 1
    INF = 10**4
    min_mp = [INF for _ in range(len(C))]
    min_mp[1] = 0
    frontier = [(0, 1)]  # (mp, number)
    while len(frontier) > 0:
        mp, n = heapq.heappop(frontier)
        for next_n in range(len(C)):
            if next_n == n:
                continue
            if min_mp[next_n] > mp + C[next_n][n]:
                # use C[next_n][n] (not C[n][next_n])
                # because this procedure starts from 1 (opposite direction)
                min_mp[next_n] = mp + C[next_n][n]
                heapq.heappush(frontier, (min_mp[next_n], next_n))
    return min_mp


def main():
    H, W = list(map(int, input().split(' ')))
    C = [list(map(int, input().split(' '))) for _ in range(10)]
    A = [list(map(int, input().split(' '))) for _ in range(H)]
    min_mp = min_mp_to_one(C)
    ans = 0
    for h in range(H):
        for w in range(W):
            if A[h][w] == -1:
                continue
            ans += min_mp[A[h][w]]
    print(ans)


if __name__ == '__main__':
    main()
