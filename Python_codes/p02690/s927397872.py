x = int(input())
for i in range(400):
  for j in range(400):
    ii = i - 200
    jj = j - 200
    if ii**5 - jj**5 == x:
      print(ii,jj)
      exit()
assert false, "final"