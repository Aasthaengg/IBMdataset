s = input()
t = input()

ans = len(t)
for i in range(len(s)-len(t)+1):
  count = 0
  r = int(i)
  for j in t:
    if s[r] != j:
      count += 1
    r += 1
  
  if ans > count:
    ans = count

print(ans)