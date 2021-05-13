import sys
input = sys.stdin.buffer.readline
from itertools import permutations

def main():
    N,C = map(int,input().split())
    D = [list(map(int,input().split())) for _ in range(C)]
    col = [list(map(int,input().split())) for _ in range(N)]
    
    mod_color = [[0]*C,[0]*C,[0]*C]
    for i in range(N):
        for j in range(N):
            mod_color[(i+j)%3][col[i][j]-1] += 1

    ans = 10**10
    for x,y,z in permutations(range(C),3):
        ret = 0
        ret += sum(mod_color[0][i]*D[i][x] for i in range(C))
        ret += sum(mod_color[1][i]*D[i][y] for i in range(C))
        ret += sum(mod_color[2][i]*D[i][z] for i in range(C))
        ans = min(ans,ret)
        
    print(ans)
    
if __name__ == "__main__":
    main()
