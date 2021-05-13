import sys
input = sys.stdin.buffer.readline

def main():
    N,M = map(int,input().split())
    g_grid = [["#" for _ in range(100)] for _ in range(50)]
    h_grid = [["." for _ in range(100)] for _ in range(50)]
    
    grid = g_grid + h_grid
    
    N -= 1
    M -= 1
    for i in range(N):
        p = 2*i+1
        x = (p//100)*2
        y = p%100
        grid[x][y] = "."
        
    for i in range(M):
        p = 2*i+1
        x = -(p//100)*2-1
        y = -(p%100)
        grid[x][y] = "#"
    
    print(100,100)
    
    for i in range(100):
        L = "".join(grid[i])
        print(L)
    
if __name__ == "__main__":
    main()