x=int(input())
large_approach=x//11
short_approach=x%11

if short_approach==0:
  print(large_approach*2)
elif short_approach<=6:
  print(large_approach*2+1)
else:
  print(large_approach*2+2)