n = int(input())
a = list(map(int,input().split()))
c = 0
count4 = 0

for i in a:
  if i%4 == 0:
    count4 += 1
  if i%2 == 0:
    c += 1
only2 = c-count4
if only2 == 0 and count4 + 1 == len(a)-c:
  print('Yes')
elif count4 < len(a)-c:
  print('No')
else:
  print('Yes')