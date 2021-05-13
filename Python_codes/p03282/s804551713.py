s = input()
k = int(input())

ans = 1
for i in range(len(s)):
  if s[i] == "1":
    k -= 1
    if k == 0: break
  else:
    ans = s[i]
    break
print(ans)