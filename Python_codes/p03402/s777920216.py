#11:57
a,b = map(int,input().split())
a -= 1
b -= 1
ap = a // 50
bp = b // 50
ar = a % 50
br = b % 50
print(ap*2 + 4 + bp*2,100)
for _ in range(ap):
  print('.#' * 50)
  print('##' * 50)
print('.#' * ar + '##' * (50-ar))
print('##' * 50)
print('..' * 50)
print('.#' * br + '..' * (50-br))
for _ in range(bp):
  print('..' * 50)
  print('.#' * 50)