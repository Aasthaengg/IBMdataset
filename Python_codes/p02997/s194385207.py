n,k = map(int,input().split())
res_graph = [[1,i] for i in range(2,n+1)]
res = (n-1)*(n-2)//2

if(k > (n-2)*(n-1)//2):
    print(-1)
    exit()

tmp_edge = 2
while res!=k:
    tmp = 1
    for i in range(n-tmp_edge):
        res_graph.append([tmp_edge,tmp+tmp_edge])
        res-=1
        tmp+=1
        if res==k:
            break
    tmp_edge+=1

print(len(res_graph))
for i,j in res_graph:
    print(i,j)
