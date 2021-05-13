s = input()
w = 0
cnt = 0
for i in range(len(s)):
  if s[i] == "W":
    cnt += i-w
    w += 1
print(cnt)