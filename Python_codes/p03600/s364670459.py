import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    edge = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        edge[i][i] = 10**10
        
    ans = 0
    for i in range(N):
        for j in range(i):
            d = min(a+b for a,b in zip(edge[i],edge[j]))
            if edge[i][j] > d:
                print(-1)
                exit()
            elif edge[i][j] < d:
                ans += edge[i][j]

    print(ans)    

if __name__ == "__main__":
    main()