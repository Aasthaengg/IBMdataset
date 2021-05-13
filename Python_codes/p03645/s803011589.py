import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
    N, M = map(int,input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int,input().split())
        G[a-1].append(b-1)
    for e in G[0]:
        if N-1 in G[e]:
            print("POSSIBLE")
            exit(0)
    print("IMPOSSIBLE")

if __name__ == '__main__':
    main()
