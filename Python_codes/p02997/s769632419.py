import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

n,k = map(int,input().split())

mx=(n-1)*(n-2)//2

if mx < k:print(-1);exit()

ans=[]
for i in range(n-1):
    ans.append((i+1,n))


add=mx-k

edge=[]
for i in range(n-1):
    for j in range(i):
        edge.append((i+1,j+1))
for i in range(add):
    ans.append(edge[i])

print(len(ans))
for i in ans:
    print(*i)