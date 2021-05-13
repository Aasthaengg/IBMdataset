S = input()
List = ["Sunny", "Cloudy", "Rainy"]
res = 0
for i in range(3):
  if S == List[i]:
    res = i+1
if res == 3:
  res = 0
print(List[res])