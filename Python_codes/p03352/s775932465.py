X = int(input())
List = [1]
a =0
for i in range(2,35):
  for j in range(2,11):
    a = i**j
    if a <= 1000:
      List.append(i**j)
    else:
      break
List.sort()
k = 0
for i in range(len(List)):
  if List[i] > X:
    k = i-1
    break
  elif List[i] == X:
    k = i
    break
print(List[k])