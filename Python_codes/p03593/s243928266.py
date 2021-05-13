h,w = map(int,input().split())
lis = [0 for i in range(26)]
s = [str(input()) for i in range(h)]
for i in range(h):
  for j in range(w):
    lis[ord(s[i][j])-ord("a")] += 1
lis.sort()
cnt1 = 0
cnt4 = 0
for num in lis:
  if num % 2 == 1:
    cnt1 += 1
  cnt4 += num//4
if h % 2 == 0:
  if w % 2 == 0:
    if cnt4 == (h//2)*(w//2):
      print("Yes")
    else:
      print("No")
  else:
    if cnt1 == 0 and cnt4 >= (h//2)*(w//2):
      print("Yes")
    else:
      print("No")
else:
  if w % 2 == 0:
    if cnt1 == 0 and cnt4 >= (h//2)*(w//2):
      print("Yes")
    else:
      print("No")
  else:
    if cnt1 == 1 and cnt4 >= (h//2)*(w//2):
      print("Yes")
    else:
      print("No")
