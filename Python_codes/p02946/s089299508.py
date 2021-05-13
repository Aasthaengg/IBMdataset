K,X=map(int,input().split())
List = []
mid = 0
for i in range(-K+1,K):
  mid = X + i
  List.append(mid)
print(*List)