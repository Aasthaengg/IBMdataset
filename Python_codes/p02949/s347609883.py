import sys
input = sys.stdin.readline

def main():
    N,M,P = map(int,input().split())
    edges = []


    for _ in range(M):
        A,B,C = map(int,input().split())
        edges.append([A-1,B-1,P-C])

    reachable_from = [False for _ in range(N)]
    reachable_from[0] = True
    reachable_to = [False for _ in range(N)]
    reachable_to[N-1] = True

    for i in range(N-1):
        for edge in edges:
            if reachable_from[edge[0]]:
                reachable_from[edge[1]] = True
            if reachable_to[edge[1]]:
                reachable_to[edge[0]] = True

    edges2 = []
    for edge in edges:
        if reachable_from[edge[0]] and reachable_to[edge[1]]:
            edges2.append(edge)

    inf = 10000*(10**5)
    dist = [inf for _ in range(N)]
    dist[0] = 0

    for i in range(N):
        for edge in edges2:
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]]+edge[2]
                if i==N-1:
                    print(-1)
                    break
        else:
            continue
        break
    else:
        print(max(0,-1*dist[N-1]))

if __name__ == "__main__":
    main()
