N,M=map(int,input().split())
ListMaster=[]
for i in range(M):
  ListMaster.append(i+1)
s =set(ListMaster)
mid = set()
List = []
for i in range(N):
  List.append(list(map(int, input().split())))
for i in range(N):
  List[i].pop(0)
for i in range(N):
  mid = set(List[i])
  s = s&mid
print(len(s))