A = []

for i in range(3):
  p, q, r = map(int, input().split())
  A.append(p)
  A.append(q)
  A.append(r)
N = int(input())
c = [0] * 9
for i in range(N):
  B = int(input())
  if B in A:
    position = A.index(B)
    c[position] = 1
if c[0]==c[4]==c[8]==1 or c[2]==c[4]==c[6]==1 or c[0]==c[1]==c[2]==1 or c[3]==c[4]==c[5]==1 or c[6]==c[7]==c[8]==1 or c[0]==c[3]==c[6]==1 or c[1]==c[4]==c[7]==1 or c[2]==c[5]==c[8]==1:
  print("Yes")
else:
  print("No")
