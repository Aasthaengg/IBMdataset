n = int(input())
List = [list(map(int,input().split())) for i in range(n)]
L = []
for i in range(len(List)):
  a = List[i][1] - List[i][0] + 1
  L.append(a)
print(sum(L))