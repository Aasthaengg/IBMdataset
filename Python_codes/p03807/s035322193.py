n = int(input())
line = map(int,input().split())
odd = []
for i in line:
  if i % 2 == 1:
    odd.append(i)
if len(odd) % 2 == 0:
  print("YES")
else:
  print("NO")