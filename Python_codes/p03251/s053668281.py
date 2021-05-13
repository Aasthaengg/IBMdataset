n,m,a,b = map(int,input().split())

x = list(map(int,input().split()))
x = max(x)

y = list(map(int,input().split()))
y = min(y)
i = x
ans = ''


for i in range(a+1,b):
  # X<z<yという区間を満たしていない ので誤りその条件を付け加えるなら...
  if x<i and i<=y:
    ans = 1
if ans:
  print('No War')
else:
  print('War')