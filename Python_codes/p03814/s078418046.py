#-------------
s = input()
#-------------
N = len(s)
A = []
Z = []
for i in range(N):
  if s[i] == "A":
    A.append(i)
  if s[i] == "Z":
    Z.append(i)
    
min_A = min(A)
max_Z = max(Z)
print(max_Z-min_A+1)