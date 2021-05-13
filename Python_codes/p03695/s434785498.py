n = int(input())
a = list(map(int,input().split()))

l = [0,0,0,0,0,0,0,0,0]


for i in range(n):
  if a[i] <= 399:
    l[0] += 1
  elif 400 <= a[i] and a[i] <= 799:
    l[1] += 1
  elif 800 <= a[i] and a[i] <= 1199:
    l[2] += 1
  elif 1200 <= a[i] and a[i] <= 1599:
    l[3] += 1
  elif 1600 <= a[i] and a[i] <= 1999:
    l[4] += 1
  elif 2000 <= a[i] and a[i] <= 2399:
    l[5] += 1
  elif 2400 <= a[i] and a[i] <= 2799:
    l[6] += 1
  elif 2800 <= a[i] and a[i] <= 3199:
    l[7] += 1
  else:
    l[8] += 1
ans = 0

if n == 1 and a[0] >= 3200:
  print(1,1)
  exit()
  
for i in range(len(l)-1):
  if l[i] > 0:
    ans += 1

if ans >= 1:
  print(ans,ans + l[8])
elif ans == 0:
  print(1,l[8])
