def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M = (int(i) for i in input().split())
    H = [int(i) for i in input().split()]
    G = [set() for _ in range(N)]
    for i in range(M):
        a, b = (int(i) for i in input().split())
        G[a-1].add(b-1)
        G[b-1].add(a-1)
    ans = 0
    for a in range(N):
        if all(H[b] < H[a] for b in G[a]):
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
