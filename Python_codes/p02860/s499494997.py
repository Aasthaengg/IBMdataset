N = int(input())
S = str(input())
 
if N % 2 == 0:
  NN = int(N/2)
  for i in range(0, NN):
    if S[i] != S[i+NN]:
      print('No')
      break
  else:
    print('Yes')
    
else:
  print('No')