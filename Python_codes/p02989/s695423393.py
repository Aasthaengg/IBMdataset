n = int(input())
m = n//2
D = list(map(int, input().split()))
D.sort()
D.reverse()
if D[m-1] == D[m]:
  print(0)
  exit()
else:
  print(D[m-1]-D[m])
  exit()