A=[0]*6
for i in range(6):
  A[i]=int(input())
  
isOK=True
for i in range(5):
  for j in range(i,5):
    if(abs(A[i]-A[j]) > A[5]):
      isOK=False
      
if(isOK):
  print("Yay!")
else:
  print(":(")
