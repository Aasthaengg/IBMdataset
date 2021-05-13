n = int(input())
A = list(map(int, input().split( )))
cnt = 1

for a in A:
  if cnt == 0:continue
  if a%2 == 0:
    if a%3 !=0 and a%5 !=0:
      cnt = 0
if cnt != 0:
  print('APPROVED')
else:
  print('DENIED')