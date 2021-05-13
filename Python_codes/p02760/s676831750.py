bingo = []
sheet = set()
for _ in range(3):
  lst = [int(i) for i in input().split()]
  bingo.append(lst)
n = int(input())
for _ in range(n):
  a = int(input())
  for i in range(3):
    for j in range(3):
      if bingo[i][j] == a:
        num = 3 * i + j
        sheet.add(num)
if 0 in sheet and 1 in sheet and 2 in sheet:
  print('Yes')
elif 0 in sheet and 3 in sheet and 6 in sheet:
  print('Yes')
elif 0 in sheet and 4 in sheet and 8 in sheet:
  print('Yes')
elif 1 in sheet and 4 in sheet and 7 in sheet:
  print('Yes')
elif 2 in sheet and 5 in sheet and 8 in sheet:
  print('Yes')
elif 2 in sheet and 4 in sheet and 6 in sheet:
  print('Yes')
elif 3 in sheet and 4 in sheet and 5 in sheet:
  print('Yes')
elif 6 in sheet and 7 in sheet and 8 in sheet:
  print('Yes')
else:
  print('No')