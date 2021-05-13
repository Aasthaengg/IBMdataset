import sys
sys.setrecursionlimit(2147483647)


n=int(input())

c={}
tree=[set([]) for _ in range(n)]

for _ in range(n-1):
    i,j,k=map(int,input().split())
    i-=1
    j-=1
    tree[i].add(j)
    tree[j].add(i)
    c[(min(i,j),max(i,j))]=k

result=[]
q,k=map(int,input().split())

memo=[-1]*n

def DEF(z,cnt):
    global memo,tree,c
    memo[z]=cnt
    for item in tree[z]:
        if memo[item]==-1:
            DEF(item,cnt+c[(min(item,z),max(item,z))])

DEF(k-1,0)
result=[]
for item in range(q):
    a,b=map(int,input().split())
    result.append(memo[a-1]+memo[b-1])

for item in result:
    print(item)





