a, b = map(int, input().split())

ans = 0
for i in range(a, b+1):
  s = str(i)
  judge = True
  for j in range(2):
    if s[j] != s[4-j]:
      judge = False
  if judge:
    ans += 1
    
print(ans)