s = input()
w = int(input())
i = 0
ans = ''
while i < len(s):
  ans += s[i]
  i += w
print(ans)