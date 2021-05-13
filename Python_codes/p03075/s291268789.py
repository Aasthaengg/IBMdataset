antena = [0]*5
for i in range(5):
  antena[i] = int(input())
  
k = int(input())
 
for i in range(len(antena)):
  if antena[-1]-antena[i]>k:
    print(":(")
    break
else:
  print("Yay!")