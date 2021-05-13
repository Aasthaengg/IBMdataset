N = input()
A = list(map(int,input().split()))
te = len(list(set(A)))
if te % 2 == 1:
  print(te)
else:
  print(te - 1)