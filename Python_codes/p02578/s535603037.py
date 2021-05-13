N = int(input())
List = list(map(int,input().split()))
counter = 0
height = List[0]
for i in range(1,N):
  if List[i] < height:
    counter += height - List[i]
  else:
    height = List[i]
print(counter)