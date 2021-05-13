n = int(input())
pn = [int(num) for num in input().split()]

k = 0
for i in range(0, len(pn)):
    if (i+1) != pn[i]:
      k += 1

if k <= 2:
  print("YES")
else :
  print("NO")
