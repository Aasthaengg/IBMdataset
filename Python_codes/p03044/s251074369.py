import sys
sys.setrecursionlimit(10**6)
n = int(input())
edge = [[] for _ in range(n)]

for i in range(n-1):
    a,b,c=map(int, input().split())
    edge[a-1].append([b-1,c])
    edge[b-1].append([a-1,c])
#任意の点から行ける偶数の距離で行けるところを同じ色で塗る。
col = [-1]*n
visited = [0]*n

def dfs(i,c):
    visited[i]=1
    col[i] = c
    for j in edge[i]:
        if not visited[j[0]]:
            if j[1]%2==0:
                dfs(j[0],c)
            else:
                dfs(j[0],-1*c)


def main():
    dfs(0,1)
    for i in range(n):
        print(max(col[i],0))



if __name__ == '__main__':
    main()
