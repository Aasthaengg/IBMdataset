N = int(input())
S = [str(s) for s in input().split()]
if len(set(S)) == 4:
  print("Four")
else:
  print("Three")