N = int(input())
s = input()
cnt = 0
for char in s:
  if char == 'R':
    cnt += 1
  if cnt > N / 2:
    print('Yes')
    break
else:
  print('No')