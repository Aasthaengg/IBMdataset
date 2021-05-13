import sys
sys.setrecursionlimit(10**7)

n = int(input())
flag = [-1 for _ in range(n)]
la=[[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    la[a-1].append(b-1)
    la[b-1].append(a-1)

def dfs(s,d):
    global flag
    global la
    flag[s] = d + 1
    for g in la[s]:
        if flag[g] == -1:
            dfs(g,flag[s])

def main():
    global n
    global flag
    dfs(0,-1)
    distf = flag[:]
    flag = [-1 for _ in range(n)]
    dfs(n-1,-1)
    dists = flag[:]
    res = 0
    for i in range(n):
        if distf[i] <= dists[i]:
            res += 1
        else:
            res -= 1
    if res > 0:
        return "Fennec"
    else:
        return "Snuke"



print(main())