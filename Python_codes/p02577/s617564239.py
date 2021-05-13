N = int(input())

n = str(N)

c = len(n)
total = 0

for c in range(c):
  total = total + int(n[c])
  
if total % 9 == 0:
  print("Yes")
  
else :
  print("No")
