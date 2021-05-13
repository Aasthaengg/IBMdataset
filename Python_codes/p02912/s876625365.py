import heapq
N,M = map(int,input().split())
list_A = list(map(lambda x: int(x)*(-1),input().split()))	

#print(list_A)
heapq.heapify(list_A)
for i in range(M):
  
  target = heapq.heappop(list_A)
  #print("after heappop",list_A)
  
  '''負の要素の切り捨て除算は切り捨てがマイナスの方に
  行くため少しだけややこしい。'''
  heapq.heappush(list_A, (-1)*((-target) // 2))  # 要素の挿入
  #print("No.",i,"change finished",list_A)

print(-sum(list_A))


