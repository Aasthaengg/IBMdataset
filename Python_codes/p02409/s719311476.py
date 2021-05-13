N = int(input())
buildings = [[[0 for V in range(10)] for F in range(3)] for B in range(4)]
for i in range(N):
 b, f, r, num = map(int, input().split())
 buildings[b-1][f-1][r-1] += num

for i in range(4):
 for j in range(3):
  for k in range(10):
   print(" {0}".format(buildings[i][j][k]), end="")
  print()
 if i!=3:
  print("####################")