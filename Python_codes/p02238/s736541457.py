
#graphの頂点vertex(インデックス、0オリジン)を深さ優先探索。dis_time:最初に訪れた時のtimeを管理するリスト
#fin_time:その頂点に対して、探索が終わった時のtimeを管理するリスト　tmp_time:現在のtime(関数内で変更できるようにリスト)
def DPS(graph,vertex,dis_time,fin_time,tmp_time):
    tmp_time[0]+=1
    dis_time[vertex]=tmp_time[0]
    for i in range(len(graph[0])):
        if(graph[vertex][i] !=0 and dis_time[i]==0):#枝先の頂点が探索済みでなかったら、
            DPS(graph,i,dis_time,fin_time,tmp_time)
    
    tmp_time[0]+=1
    fin_time[vertex]=tmp_time[0]



#グラフの作成
n=int(input())
graph=[[0]*n for loop in range(n)]
for loop in range(n):
    tmp_ope=list(map(int,input().split()))
    for j in range(tmp_ope[1]):
        graph[tmp_ope[0]-1][tmp_ope[j+2]-1]=1


dis_time=[0]*n
fin_time=[0]*n
tmp_time=[0]
for i in range(n):
    if(dis_time[i]==0):
        DPS(graph,i,dis_time,fin_time,tmp_time)

for i in range(n):
    print(f"{i+1} {dis_time[i]} {fin_time[i]}")
