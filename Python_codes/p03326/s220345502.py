import sys
input=sys.stdin.readline
INF = 10**9

def main():
    n,m=map(int,input().split())
    cake=[list(map(int,input().split())) for _ in range(n)]
    
    op = [(1,1,-1),(1,-1,-1),(1,1,-1),(-1,-1,-1),(1,1,-1),(1,-1,-1),(1,1,-1)]

    ans =0 
    for i in range(8):
        cake.sort(key=lambda x:sum(x),reverse=True)
        t = 0
        for k in range(3):
            t += abs(sum([cake[j][k] for j in range(m)]))
        ans = max(ans,t)
        if i!=7:
            cake = [[cake[j][0]*op[i][0],cake[j][1]*op[i][1],cake[j][2]*op[i][2]] for j in range(n)]
    
    print(ans)  
if __name__=='__main__':
    main()
