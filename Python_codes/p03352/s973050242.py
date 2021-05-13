def solve():
  ans = 0
  X = int(input())
  lis = [False]*(X+1)
  lis[1] = True
  for b in range(2,X+1):
    p = 2
    while b**p<=X:
      lis[b**p] = True
      p += 1
  for i in range(X,-1,-1):
    if lis[i]==True:
      return i
print(solve())