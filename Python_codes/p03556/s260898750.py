n = int(input())
while True:
  sq = n**0.5
  if sq.is_integer():
    break
  else:
    n-=1
print(n)