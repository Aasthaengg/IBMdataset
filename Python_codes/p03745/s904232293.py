n=int(input())
a=list(map(int,input().split()))
flg = 0
ans=1
for i in range(1,n):
  tmp = a[i-1]
  if a[i] == tmp:
    pass
  elif a[i] > tmp:
    if flg == 1:
      pass
    elif flg == -1:
      ans += 1
      flg = 0
    else:
      flg = 1
  else:
    if flg == -1:
      pass
    elif flg == 1:
      ans += 1
      flg = 0
    else:
      flg = -1
print(ans)