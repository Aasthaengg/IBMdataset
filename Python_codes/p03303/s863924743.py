s = input()
w = int(input())
ans = ''
count = 0
while count <= len(s)-1:
  ans += s[count]
  count += w
print(ans)