s = int(input())
if s % 2 == 1:
  Odd = (s+1)/2
  Even = Odd -1
else:
  Odd = s/2
  Even = Odd
res= int(Odd) * int(Even)
print(res)