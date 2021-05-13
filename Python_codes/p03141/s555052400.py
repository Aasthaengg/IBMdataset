def f():
    import sys
    input=sys.stdin.buffer.readline
    sys.setrecursionlimit(10**9)
    n=int(input())
    l=sorted([list(map(int,input().split())) for i in range(n)],key=sum,reverse=1)
    ans=0
    for i in range(n):
        if i%2:ans-=l[i][1]
        else:ans+=l[i][0]
    print(ans)
if __name__ == "__main__":
    f()