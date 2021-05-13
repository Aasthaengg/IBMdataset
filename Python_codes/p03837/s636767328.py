import heapq
class Graph():
    def __init__(self,vertex_num,node_num,naive_input,start_zero=True,direction=False):
        self.vertex_num=vertex_num
        self.node_num=node_num
        #nodeには入力時のインデックスも含む
        #[接続ノード , インッデクス]のarray
        node=[{} for _ in range(vertex_num)]
        for i in range(node_num):
            u,v,w=naive_input[i]
            if not start_zero:
                u-=1
                v-=1
            node[u][v]={"weight":w,"index":i}
            #node[v][u]={"weight":w,"index":i}
            if not direction:
                node[v][u]={"weight":w,"index":i}
                #node[u][v]["reverse"]={"weight":w,"index":i}
        self.node=node
        #それぞれの頂点の辺の数
        self.node_num_arr=list(map(lambda x:len(x),node))

    def djikstra(self,s=0):
        distance=[float("inf") for _ in range(self.vertex_num)]
        distance[s]=0
        #visitedにしたけど正確には訪問済みではなく最短距離確定済みが適切
        #いい名前教えて
        #visited_vertex=[False for _ in range(self.vertex_num)]
        #visited_vertex[s]=True
        visited_vertex={s}
        before_vertex=[float("inf") for _ in range(self.vertex_num)]
        node_index_arr=[float("inf") for _ in range(self.vertex_num)]
        while len(visited_vertex)<self.vertex_num:
            #will_visit_node=cal_will_visit_node(self.node,visited_vertex)
            will_visit_node=set()
            for now_node_num in visited_vertex:
                for next_node_num in self.node[now_node_num].keys():
                    if next_node_num in visited_vertex:
                        continue
                    will_visit_node.add(next_node_num)
                    next_node=self.node[now_node_num][next_node_num]
                    cal_d=distance[now_node_num]+next_node["weight"]
                    if cal_d<distance[next_node_num]:
                        distance[next_node_num]=cal_d
                        before_vertex[next_node_num]=now_node_num
                        node_index_arr[next_node_num]=next_node["index"]
                    #distance_vertex[distance[next_node_num]]=next_node_num
                    #heapq.heappush(min_distance_heap,distance[next_node_num])
            #add_vertex=distance_vertex[min_distance_heap[0]]
            add_vertex=[float("inf"),float("inf")]
            for i in will_visit_node:
                if distance[i]<add_vertex[1]:
                    add_vertex[0]=i
                    add_vertex[1]=distance[i]
            visited_vertex.add(add_vertex[0])
        return node_index_arr
        





n,m=list(map(int,input().split()))
a=[list(map(int,input().split())) for _ in range(m)]
G=Graph(n,m,a,start_zero=False)  
ans=[True for _ in range(m)]
for i in range(n):
    tmp=G.djikstra(i)
    for j in tmp:
        if j!=float("inf"):
            ans[j]=False

print(sum(ans))

            
