import sys
def main():
    input = sys.stdin.readline
    N=int(input())
    A=[int(input()) for _ in range(N)]

    if A[0]!=0:
        print(-1)
        exit()
    ans=0
    d=0
    for i in range(1,N):
        if A[i]==0: continue
        if A[i]>d+1:
            print(-1)
            exit()
        d=A[i]
        if A[i]==A[i-1]+1:
            ans+=1
        else:
            ans+=A[i]

    print(ans)

if __name__ == '__main__':
    main()