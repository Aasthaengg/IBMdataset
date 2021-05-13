def main():
    n=int(input())
    ab=[list(map(int,input().split())) for _ in [0]*(n-1)]
    c=sorted(list(map(int,input().split())),reverse=True)
    g=[set() for _ in [0]*n]
    [g[a-1].add(b-1) for a,b in ab]
    [g[b-1].add(a-1) for a,b in ab]
    l=[]
    print(sum(c)-max(c))
    for i in range(n):
        if len(g[i])==1:
            l.append(i)
    ans_l=[0]*n
    while l:
        i=l.pop()
        ans_l[i]=c.pop()
        for j in g[i]:
            g[j].remove(i)
            if len(g[j])==1:
                l.append(j)
        g[i]=set()
    print(*ans_l)
main()