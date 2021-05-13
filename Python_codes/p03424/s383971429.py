N = int(input())
A = list(map(str,input().split()))
S = set(A)
if len(S) == 4:
  print("Four")
else:
  print("Three")