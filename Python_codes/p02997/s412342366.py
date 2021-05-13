from itertools import combinations


def main():
    N, K = list(map(int, input().split(' ')))
    if K > (N - 1) * (N - 2) // 2:
        print(-1)
        return
    # print M and graph
    adj_nodes = [[] for _ in range(N)]
    adj_nodes[0] = [n for n in range(1, N)]
    C = (N - 1) * (N - 2) // 2 - K
    c = 0
    for comb in combinations(range(1, N), 2):
        if c >= C:
            break
        u, v = comb
        adj_nodes[u].append(v)
        c += 1
    print(N - 1 + C)
    for u in range(N):
        for v in adj_nodes[u]:
            print('{} {}'.format(u + 1, v + 1))


if __name__ == '__main__':
    main()