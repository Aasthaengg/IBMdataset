s = str(input())
t = str(input())
cnt = 0
for i in range(0,3):
  if s[i] == t[i]:
    cnt += 1
print(int(cnt))