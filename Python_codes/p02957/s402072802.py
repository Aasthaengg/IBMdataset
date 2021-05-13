a,b=map(int,input().split())
count = 0
num = 0
for i in range(int((a+b)/2)-5, int((a+b)/2)+5):
  if abs(a-i) == abs(b-i):
    count += 1
    num = i
if count > 0:
  print(num)
else:
  print("IMPOSSIBLE")