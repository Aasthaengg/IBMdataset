N=int(input())
D,X=map(int,input().split())
res = X
List = []
for i in range (N):
  List.append(int(input()))
for i in range(N):
  for i in range(1,D+1,List[i]):
    res += 1
print(res)