import sys
input = sys.stdin.buffer.readline

def main():
    H,W,D = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(H)]
    pos = [[-1,-1] for _ in range(H*W)]
    for i in range(H):
        for j in range(W):
            pos[a[i][j]-1][0] = i
            pos[a[i][j]-1][1] = j
    
    def manhattan_dist(x1,y1,x2,y2):
        return abs(x2-x1)+abs(y2-y1)

    ans_list = [[0] for _ in range(D)]
    for i in range(D):
        do = -(-(H*W-i)//D)
        for j in range(do-1):
            x1,y1 = pos[D*j+i]
            x2,y2 = pos[D*(j+1)+i]
            md = manhattan_dist(x1,y1,x2,y2)
            ans_list[i].append(ans_list[i][-1]+md)
    
    Q = int(input())
    for _ in range(Q):
        a,b = map(int,input().split())
        mod = a%D-1
        u = -(-a//D)-1
        w = -(-b//D)-1
        print(ans_list[mod][w]-ans_list[mod][u])

if __name__ == "__main__":
    main()
