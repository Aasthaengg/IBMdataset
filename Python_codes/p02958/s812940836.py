N = int(input())
P = list(map(int,input().split()))
A = []
y = 0

for n in range(1,N+1):
  A.append(n)

for p,a in zip(P,A):
  if p!=a:
    y+=1
    

if y<3:
  print("YES")
else:
  print("NO")