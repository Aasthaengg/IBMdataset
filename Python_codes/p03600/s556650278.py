# ABC074D

import sys
input=sys.stdin.readline

def main():
    N=int(input())
    A=[tuple(map(int,input().split())) for i in range(N)]
    
    ans=0
    for i in range(N):
        for j in range(i+1,N):
            ans+=A[i][j]
            for k in range(N):
                if i!=k and j!=k:
                    if A[i][j]>A[i][k]+A[k][j]:
                        print(-1)
                        exit()
                    elif A[i][j]==A[i][k]+A[k][j]:
                        ans-=A[i][j]
                        break
                    
    print(ans)
    
    
if __name__=="__main__":
    main()
