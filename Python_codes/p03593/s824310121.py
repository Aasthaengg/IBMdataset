H, W = map(int, input().split())

lst = [0]*26

for _ in range(H):
  s = input()
  for c in s:
    lst[ord(c)-ord('a')] += 1
  
cnt1 = 0
cnt2 = 0
for i in lst:
  if i%2 != 0:
    cnt1 += 1
  elif i%4 != 0:
    cnt2 += 1
    
if cnt1 > 1:
  print('No')
  exit()
  
if H%2 == 0 and W%2 == 0:
  if cnt1 > 0 or cnt2 > 0:
    print('No')
  else:
    print('Yes')
elif H%2 == 1 and W%2 == 0:
  if cnt1 > 0 or cnt2 > W//2:
    print('No')
  else:
    print('Yes')
elif H%2 == 0 and W%2 == 1:
  if cnt1 > 0 or cnt2 > H//2:
    print('No')
  else:
    print('Yes')
else:
  if cnt2 > (H//2 + W//2):
    print('No')
  else:
    print('Yes')