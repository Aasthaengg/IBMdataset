N = list(map(int,input().split()))
N.sort()
if sum(N[:2]) == N[2]:
  print("Yes")
else:
  print("No")