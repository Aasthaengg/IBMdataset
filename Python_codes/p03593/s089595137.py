h,w = map(int, input().split())
a = [input() for i in range(h)]
cnt = [0] * 26
for i in a:
  for j in i:
    cnt[ord(j)-ord("a")] += 1
two,no = 0,0
for i in cnt:
  if i % 2:
    no += 1
  elif i % 4:
    two += 1
if (h % 2) and (w % 2):
  if no <= 1 and two <= h//2 + w//2:
    print("Yes")
  else:
    print("No")
elif (h % 2):
  if no == 0 and two <= w//2:
    print("Yes")
  else:
    print("No")
elif (w % 2):
  if no == 0 and two <= h//2:
    print("Yes")
  else:
    print("No")
else:
  if no == 0 and two == 0:
    print("Yes")
  else:
    print("No")