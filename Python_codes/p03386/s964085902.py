MM = input().split()
A = int(MM[0])
B = int(MM[1])
K = int(MM[2])
MM = set()
for i in range(A, A+K):
  if i <= B:
    MM.add(i)
for i in reversed(range(B-K+1,B+1)):
  if i >= A:
    
    MM.add(i)

MM = sorted(MM)

for i in MM:
  print(i)