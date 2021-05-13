import sys
sys.setrecursionlimit(10**6)


def DFS(num,pre):
    global point
    if color[num]=="white":
        A[num]=C.pop()
        point +=min(A[num],pre)
        color[num]="black"
        for i in tree[num]:
            DFS(i,A[num])


n=int(input())
AB=[list(map(int,input().split())) for _ in range(n-1)]
C=sorted(list(map(int,input().split())))

color=["white" for _ in range(n+1)]
tree=[[] for _ in range(n+1)]
for a,b in AB:
    tree[a].append(b)
    tree[b].append(a)

A=[0 for _ in range(n+1)]
point=0
DFS(1,0)

print(point)
print(*A[1:])