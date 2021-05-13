n = int(input())
a, b = [int(i) for i in input().split()]
numlist = [int(i) for i in input().split()]

cntx = 0
cnty = 0
cntz = 0

for i in range(n):
  if numlist[i]<=a:
    cntx += 1
  elif numlist[i]<=b:
    cnty += 1
  else:
    cntz += 1
 
print(min([cntx, cnty, cntz]))