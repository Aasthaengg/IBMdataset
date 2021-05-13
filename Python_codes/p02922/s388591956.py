a,b = map(int,input().split())
cnt1 = a
cnt2 = 1
ans = 0

if b == 1:
  print("0")
else:
  while cnt1 < b:
    cnt1 += (a-1)
    cnt2 += 1
  print(cnt2)