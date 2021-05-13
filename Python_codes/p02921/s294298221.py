f = input()
r = input()
 
cnt = 0
for i in range(3):
  if f[i] == r[i]:
    cnt += 1
print(cnt)