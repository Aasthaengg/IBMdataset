s = str(input())
t = str(input())
l = len(s)
cnt = 0

for i in range(l):
  if s[i] != t[i]:
    cnt += 1

print(cnt)