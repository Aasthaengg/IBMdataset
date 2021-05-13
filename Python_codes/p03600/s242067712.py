import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    #print(a)

    for k in range(n-1,-1,-1):
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):            
                #print(k,i,j,a)
                if (i==j or k==i or k==j):
                    continue
                if (a[i][k]!=-1 and a[k][j]!=-1 and a[i][j] == a[i][k]+a[k][j]):
                    a[i][j] = -1
                elif (a[i][k]!=-1 and a[k][j]!=-1 and a[i][j] > a[i][k]+a[k][j]):
                    print(-1)
                    exit()
            
    #print(a)

    ans = 0
    for i in range(0,n-1):
        for j in range(i,n):
            if (a[i][j]!=-1):
                ans += a[i][j]
    print(ans)
    
if __name__=="__main__":
    main()
