k,t = map(int,input().split())
a = list(map(int,input().split()))
maxa = max(a)
if t == 1:
  print(k-1)
  exit()
if k//2 >= maxa:
  print(0)
else:
  print(maxa-(k-maxa)-1)