s = input()
ans = 642

for i in range(len(s)-2):
  if ans > abs(int(s[i:i+3])-753):
    ans = abs(int(s[i:i+3])-753)
  else:
    ans = ans

print(ans)