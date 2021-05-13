A = list(map(int, input().split()))
A.append(sum(A))

ans = False
for i in A:
  if i%3 == 0:
    ans = True
if ans:
  print("Possible")
else:
  print("Impossible")