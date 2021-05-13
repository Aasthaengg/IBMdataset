import sys
S = input()
cnt=0
for i in range(len(S)):
  if S[i] == 'x':
    cnt += 1
  if cnt >= 8:
    print('NO')
    sys.exit()
print('YES')