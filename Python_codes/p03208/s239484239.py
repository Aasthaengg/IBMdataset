N,K=map(int,input().split())
List = []
for i in range (N):
  List.append(int(input()))
List.sort()
res = 10000000000000
for i in range(N-K+1):
  res = min(res, List[i+K-1]-List[i])
print(res)