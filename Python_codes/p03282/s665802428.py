s = input()
k = int(input())
cnt = 0
for l in s:
  if l!='1':
    break
  cnt += 1
if cnt>=k:
  print(1)
else:
  print(s[cnt])