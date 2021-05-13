List = []
for i in range (3):
  List.append(int(input()))
X=int(input())
res = 0
c = 0
for i in range(List[0]+1):
  for j in range(List[1]+1):
    c = int(X/50) - 10 * i - 2 * j
    if 0<= c <= List[2]:
      res+=1
print(res)