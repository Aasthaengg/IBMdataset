import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    a=ord('a')
    s=list(map(lambda x:ord(x)-a,input()))
    N=len(s)
    t=list(map(lambda x:ord(x)-a,input()))
    l=[[-1]*26 for _ in range(len(s))]
    for i in range(N-1,-N,-1):
        for j in range(26):
            if s[i]==j:
                l[i-1][j]=i%N
            else:
                l[i-1][j]=l[i][j]
    ans=0
    index=N-1
    for a in t:
        n=l[index][a]
        if n==-1:
            print(-1)
            exit()
        if n>index:
            ans+=n-index
        else:
            ans+=n+N-index
        index=n
    print(ans)

if __name__ == '__main__':
    main()
