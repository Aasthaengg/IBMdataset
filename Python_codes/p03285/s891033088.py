buy = [False]*1000
buy[0] = True
for i in range(100):
  if buy[i]:
    buy[i+4] = True
    buy[i+7] = True
    
n = int(input())
if buy[n]:
  print("Yes")
else:
  print("No")