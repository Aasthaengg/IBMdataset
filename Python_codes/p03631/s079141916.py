n = input()
N = len(n)
x=[]
y=[]
for i in range(N):
  x.append(n[i])
for j in reversed(range(N)):
  y.append(n[j])

if x==y:
  print("Yes")
else:
  print("No")