from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,m=map(int,readline().split())
    G=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b=map(int,readline().split())
        G[a].append(b)
        G[b].append(a)

    s=set(G[1])
    ans=False
    while len(s)>0:
        now=s.pop()
        for nex in G[now]:
            if nex==n:
                ans=True
                break

    print("POSSIBLE" if ans else "IMPOSSIBLE")

if __name__=="__main__":
    main()