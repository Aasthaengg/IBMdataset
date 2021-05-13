n = int(input())
a = list(map(int,input().split()))
cnt_2 = []
cnt_4 = []
for i in a:
  if i%4 == 0:
    cnt_4.append(i)
  elif (i%4 != 0) and (i%2 == 0):
    cnt_2.append(i)
if len(cnt_2) == 0:
  if len(cnt_4)*2+1 >= n:
    print('Yes')
  else:
    print('No')
else:
  if len(cnt_2)+len(cnt_4)*2 >= n:
    print('Yes')
  else:
    print('No')