n = input()
an = [int(num) for num in input().split()]
an_unique = list(set(an))

if len(an) == len(an_unique):
  print("YES")
else :
  print("NO")