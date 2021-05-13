import sys
sys.stdin.readline

def main():
    N, M = map(int, input().split())
    ABC = [tuple(map(int, input().split())) for _ in range(M)]
    INF = float("inf")
    cost = [-INF] * N
    cost[0] = 0
    for i in range(N-1):
        for a, b, c in ABC:
            cost[b-1] = max(cost[b-1], cost[a-1] + c)
    prev = cost[N-1]
    for a, b, c in ABC:
        cost[b-1] = max(cost[b-1], cost[a-1] + c)    
    print(cost[N-1] if cost[N-1] == prev else "inf")

if __name__ == "__main__":
    main()