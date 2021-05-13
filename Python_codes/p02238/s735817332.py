def main():

    inf = 1000000007
    n = int(input())
    e = [[] for _ in range(n)]
    d = [inf]*n
    f = [inf]*n
    step = 1

    def dfs(v):
        nonlocal step
        d[v] = step
        step+=1
        for u in e[v]:
            if d[u] == inf:dfs(u)
        f[v] = step
        step +=1

    e = [[] for _ in range(n)]
    for i in range(n):
        m = list(map(int,input().split()))
        for j in range(2,len(m)):
            e[m[0]-1].append(m[j]-1)
    for i in range(n):
        if d[i]==inf:dfs(i)
    for i in range(n):
        print (i+1,d[i],f[i])

if __name__ == '__main__':
    main()


