s = input()
cnt = 1000000000000000000
for i in range(len(s)-2):
  j = abs(753 - int(s[i]+s[i+1]+s[i+2]))
  if cnt > j:
    cnt = j
print(cnt)
