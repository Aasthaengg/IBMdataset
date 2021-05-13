a = input()
cnt = 0
for i in range(len(a)):
  if i == 0:
    continue
  if a[i] != a[i-1]:
    cnt += 1
print(cnt)