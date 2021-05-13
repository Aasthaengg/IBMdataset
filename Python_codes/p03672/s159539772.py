s = input()
ans = 0
for i in range(len(s) // 2 - 1):
  if s[:i * 2 + 2] == s[:i+1] + s[:i+1]:
    ans = 2 * i +2
print(ans)