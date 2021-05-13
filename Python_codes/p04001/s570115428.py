X = str(input())
n = len(X)-1
ans = 0

for i in range(2**n):
  l = X[0]
  for j in range(n):
    if (i>>j & 1) == 1:
      l += "+"
    l += X[j+1]
  #Xのjが入ってる番目の隙間でsplit
  num = map(int,l.split("+"))
  ans += sum(num)
print(ans)
