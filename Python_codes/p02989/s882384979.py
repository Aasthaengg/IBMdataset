n = int(input())
D = list(map(int, input().split()))
D.sort()
if D[n//2-1] == D[n//2]:
  print(0)
else:
  print(D[n//2] - D[n//2-1])