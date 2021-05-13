def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M = (int(i) for i in input().split())
    G = [[] for i in range(N)]
    for i in range(M):
        x, y = (int(i)-1 for i in input().split())
        G[x].append(y)
        G[y].append(x)

    for i in range(N):
        if len(G[i]) % 2:
            return print("NO")
    else:
        return print("YES")


if __name__ == '__main__':
    main()
