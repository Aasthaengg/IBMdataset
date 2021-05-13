A = list(map(int, input().split()))
if sum(A) >= 24 :
  print(sum(A) - 24)
else :
  print(sum(A))