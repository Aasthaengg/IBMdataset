import sys
input=sys.stdin.readline

def warshallFloyd(V, dp):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

def main(args):
    H,W = map(int,input().split())
    cost = [[0] for _ in range(10)]
    for i in range(10):
        cost[i] = list(map(int,input().split()))
    
    wall = [[] for _ in range(H)]
    for i in range(H):
        wall[i] = list(map(int,input().split()))
    
    warshallFloyd(10, cost)
    
    cost_to_one = [0]*10
    for i in range(10):
        cost_to_one[i] = cost[i][1]
    
    #print(cost_to_one)
      
    ans = 0
    for i in range(H):
        for j in range(W):
            if wall[i][j] != -1:
                ans += cost_to_one[wall[i][j]]
    
    print(ans)
    
if __name__ == '__main__':
    main(sys.argv[1:])