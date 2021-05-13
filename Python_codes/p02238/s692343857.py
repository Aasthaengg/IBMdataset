import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

G = [[] for _ in range(105)]
begin = [-1] * 105
end = [-1] * 105

t = 1
def dfs(v):
    global t
    begin[v] = t
    t += 1
    for e in G[v]:
        if begin[e] < 0:
            dfs(e)
    end[v] = t
    t += 1

def main():
    N = int(input())
    for i in range(N):
        A = list(map(int,input().split()))
        for a in A[2:]:
            G[i].append(a - 1)
    
    for i in range(N):
        if begin[i] < 0:
            dfs(i)
    for i in range(N):
        print(i + 1,begin[i],end[i])
if __name__ == '__main__':
    main()
