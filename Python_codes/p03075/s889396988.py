x = [0]*5

for i in range(5):
  x[i] = int(input())
  
k = int(input())
#print(k,x)
for i in range(5):
  for j in range(i,5):
    if(x[j] - x[i]  > k):
      print(":(")
      exit()
print("Yay!")