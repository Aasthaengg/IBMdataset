import sys
sys.setrecursionlimit(2147483647)



n=int(input())

uvw={}
tree=[[] for _ in range(n)]
for _ in range(n-1):
    u,v,w=list(map(int,input().split()))
    uvw[(u-1,v-1)]=w
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)
    #u<v

result=[-1]*n
#print(tree)
def DEF(x,dis):
    #print("x",x)
    global tree, uvw,result
    for nextNode in tree[x]:
        if result[nextNode]==-1:
            nextDis=dis+uvw[(min(x,nextNode),max(x,nextNode))]
            if (nextDis)%2==0:
                result[nextNode]=0
                DEF(nextNode,nextDis)
            else:
                result[nextNode]=1
                DEF(nextNode,nextDis)
result[0]=0
DEF(0,0)

for item in result:
    print(item)