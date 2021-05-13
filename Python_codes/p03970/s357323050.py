a = 'CODEFESTIVAL2016'
b = input()
ans = 0
for i in range(len(a)):
  if a[i] != b[i]:
    ans += 1
print(ans)