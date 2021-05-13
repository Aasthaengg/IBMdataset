import heapq
X,Y,Z,K = map(int,input().split())

limit = [X,Y,Z]

nums = []
heapq.heapify(nums)
num = 0
abc = [[] for i in range(3)]

for i in range(3):
  abc[i] = sorted(list(map(int,input().split())),reverse = True)
  num += abc[i][0] * -1
  
heapq.heappush(nums,[num,0,0,0])
yet = []

for i in range(K):
  M = heapq.heappop(nums)
  for j in range(3):
    ID = M[1:]
    ID[j] += 1
    if ID[j] < limit[j]:
      a = ID[0]
      b = ID[1]
      c = ID[2]
      m = (abc[0][a] + abc[1][b] + abc[2][c]) * - 1
      if ID not in yet:
        heapq.heappush(nums,[m,a,b,c])
        yet.append(ID)
  print(M[0] * -1)
  
