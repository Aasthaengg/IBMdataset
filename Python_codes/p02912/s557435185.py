import heapq
N,M = map(int,input().split())
list_A = list(map(int,input().split()))	
list_A = list(map(lambda x: int(x)*(-1),list_A))

#print(list_A)

#heapifyが動作が重い。for文の中に入れるとTLE。
heapq.heapify(list_A) #list_Aを優先度付きキューに
for i in range(M):
  
  target = heapq.heappop(list_A)
  #print("after heappop",list_A)
  
  '''負の要素の切り捨て除算は切り捨てがマイナスの方に
  行くため少しだけややこしい。'''
  target = (-1)*((-target) // 2)
  heapq.heappush(list_A, target)  # 要素の挿入
  #print("No.",i,"change finished",list_A)

print((-1)*sum(list_A))


