def main():
    import sys
    input=sys.stdin.readline   
    sys.setrecursionlimit(100000000)

    n=int(input())
    point=[tuple(map(int,input().split())) for _ in range(n)]
    dic={i:j for i,j in zip(point,range(n))}
    
    if n==1:
        print(1)
        exit()
        
    ans=10**9
    for i in range(n-1):
        for j in range(i+1,n):
            p=point[j][0]-point[i][0]
            q=point[j][1]-point[i][1]
            cnt=0
            visited=[True]*n

            def dfs(x,y):
                if (x+p,y+q) in dic:
                    idx=dic[(x+p,y+q)]
                    if visited[idx]:
                        visited[idx]=False
                        dfs(x+p,y+q)
                if (x-p,y-q) in dic:
                    idx=dic[(x-p,y-q)]
                    if visited[idx]:
                        visited[idx]=False
                        dfs(x-p,y-q)

            for k in range(n):
                if visited[k]:
                    visited[k]=False
                    cnt+=1
                    dfs(point[k][0],point[k][1])      
        
            ans=min(ans,cnt)  
    print(ans)

if __name__=='__main__':
    main()