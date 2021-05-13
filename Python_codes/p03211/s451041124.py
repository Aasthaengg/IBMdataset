N = input()
L = []
A = []

for i in range (len(N)-2):
  L.append(N[i]+N[i+1]+N[i+2])
  
for j in range(len(L)):
  A.append(abs(int(L[j])-753))
  
print(min(A))