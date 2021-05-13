a = int(input())

l = list(map(int, input().split()))
s_l = sorted(l)

big = s_l[a-1]
small = 0

for i in range(a-1):
  small += s_l[i]
if big < small:
  print('Yes')
else:
  print('No')