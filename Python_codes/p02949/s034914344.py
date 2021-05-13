import sys
def main():
    N, M, P = map( int, input().split())
    INF = 1e18
    d = list()
    for _ in range(M):
        a, b, c = map( int, input().split())
        a, b = a-1, b-1
        d.append((a,b,P-c))
    V = [INF]*N
    V[0] = 0
    for _ in range(N):
        for (s,t,cost) in d:
            if V[s] != INF:
                V[t] = min(V[t], V[s] + cost)

    for _ in range(N):
        for (s,t,cost) in d:
            if V[s] != INF:
                if V[t] > V[s] + cost:
                    V[t]=-INF

    if V[-1] == -INF:
        print(-1)
    else:
        print( max(-V[-1], 0))
if __name__ == '__main__':
    main()
