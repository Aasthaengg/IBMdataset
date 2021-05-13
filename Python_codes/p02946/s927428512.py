def resolve():
    k,x=map(int,input().split())
    ans=list(range(max(-10**6,x-k+1),min(10**6,x+k-1)+1))
    print(*ans,sep=' ')

if __name__ == '__main__':
    resolve()