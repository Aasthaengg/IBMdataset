a = list('CODEFESTIVAL2016')
b = list(input())
cnt = 0
for i in range(len(a)):
  if b[i] != a[i]:
  	cnt += 1
print(cnt)