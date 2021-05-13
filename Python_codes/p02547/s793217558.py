import sys
N =int(input())
D = []
for i in range(N):
  d_1,d_2 = map(int,input().split())
  D.append([d_1,d_2])
for x in range(N-2):
  if D[x][0]==D[x][1] and D[x+1][1]==D[x+1][0] and D[x+2][1]==D[x+2][0]:
    print("Yes")
    sys.exit()
print("No")
