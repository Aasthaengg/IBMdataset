s = list(input())
d = 'CODEFESTIVAL2016'
l = list(d)

cnt =0
for i in range(len(s)):
  if l[i] != s[i]:
    cnt +=1
print(cnt)