S = str(input())
T = str(input())

cnt = 0

for i in range(3):
  if S[i] == T[i]:
    cnt += 1
  else:
    pass
print(cnt)