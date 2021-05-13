N,A,B = map(int,input().split())
List = list(map(int,input().split()))
cost = []
for i in range(N-1):
  cost.append(min(A*(List[i+1]-List[i]),B))
Answer = sum(cost)
print(Answer)