n = input()
ans = 0
for i in set(n):
  if n.count(i) % 2 == 0:
    ans += 1
    
if ans == len(set(n)):
  print("Yes")
else:
  print("No")
