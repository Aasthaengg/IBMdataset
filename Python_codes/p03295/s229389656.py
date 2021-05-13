## coding: UTF-8
##区間スケジューリング問題

N,M = map(int,input().split())

graph = []
for i in range(M):
    graph.append(list(map(int, input().split())))
#print(graph)

itv = []
for i in range(M):
    itv.append([graph[i][1] - 1, graph[i][0]])

itv = sorted(itv)
#print(itv)

tt = 0 #終点を保持
ans = 0
for i in range(M):
    #print('i:{},tt:{}, itv[i]:{}'.format(i, tt, itv[i]))
    #起点が現状の終点よりも後ろだったらその区間は満たしてやらないといけない
    #満たすのはその区間の終点でいい。なぜなら終点でソートしているので、その区間の終点を満たしてやったとしてもでこれから先に出てくる区間を抜かしてしまうことはないし、最大効率で他の区間も充たせるから
    if(itv[i][1] > tt):
        tt = itv[i][0]
        ans += 1
        #print('ans:{}, tt:{}'.format(ans, tt))
print(ans)

