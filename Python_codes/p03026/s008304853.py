import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N = I()
Graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = MI()
    Graph[a].append(b)
    Graph[b].append(a)
C = LI()
C.sort(reverse=True)
print(sum(C[1:]))

ANS = [-1]*(N+1)
index = 0


def dfs(x,i):
    global index
    ANS[x] = C[i]
    for y in Graph[x]:
        if ANS[y] == -1:
            index += 1
            dfs(y,index)


dfs(1,0)
print(*ANS[1:])
