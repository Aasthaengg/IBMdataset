k = int(input())
a, b = map(int,input().split())
i = a
ans = 0
while (i <= b):
  if(i%k == 0):
    ans = 1
  i = i + 1
if (ans == 0):
  print("NG")
else:
  print("OK")