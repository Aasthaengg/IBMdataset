n = int(input())
l = sorted(list(map(int, input().split())), reverse=True)
cnt = 0
for i in l[1:]:
  cnt += i
if cnt > l[0]:
  print('Yes')
else:
  print('No')