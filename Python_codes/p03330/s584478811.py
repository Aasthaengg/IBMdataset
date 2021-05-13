from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,max_c=map(int,readline().split())
    d=[list(map(int,readline().split())) for _ in range(max_c)]
    c=[list(map(lambda x:int(x)-1,readline().split())) for _ in range(n)]

    #前処理
    color_table=[[0]*max_c for _ in range(3)]
    for color in range(max_c):
        for i in range(n):
            for j in range(n):
                color_table[(i+j+2)%3][color]+=d[c[i][j]][color]

    #全探索
    ans=float("inf")
    for i in range(max_c):
        for j in range(max_c):
            for k in range(max_c):
                if i==j or j==k or k==i:
                    continue
                ans=min(ans,color_table[0][i]+color_table[1][j]+color_table[2][k])

    print(ans)

if __name__=="__main__":
    main()