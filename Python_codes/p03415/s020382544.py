C = list(input() for i in range(3))

S=''
for i in range(3):
  S=S+C[i][i]
  
print(S)