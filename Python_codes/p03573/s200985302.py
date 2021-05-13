List = list(map(int, input().split()))
res = 0
for i in range(2):
  for j in range(i+1,3):
    if List[i] == List[j]:
      res = 3 - i - j
print(List[res])