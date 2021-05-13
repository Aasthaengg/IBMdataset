H,W = map(int,input().split())
dic = {}
for h in range(H):
  s = list(input())
  for x in s:
    dic[x] = dic.get(x,0) + 1

c1 = 0
c2 = 0
for x in dic.values():
  if x%2 == 1:
    c1 += 1
    x -= 1
  if x%4 == 2:
    c2 += 1
if c1>(H%2)*(W%2):
  print("No")
elif c2>((W*(H%2))//2)+((H*(W%2))//2):
  print("No")
else:
  print("Yes")
