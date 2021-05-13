S = input()
T = input()
x = 0
 
for i in range(3):
  if S[i] == T[i]:
  	x = x + 1
  else:
  	x = x
print(x)