S = input()
T = input()
cnt = 0
loop = 0
for i in S:
  if i == T[loop]:
    cnt += 1
  loop += 1
print(cnt)