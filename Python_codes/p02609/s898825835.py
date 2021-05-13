n = int(input())
x = input()
cnt1 = x.count('1')
x10 = int(x,2)

if cnt1 > 1:
  x10mod_m = x10 % (cnt1-1)
  x10mod_p = x10 % (cnt1+1)
else:
  x10mod_m = 0
  x10mod_p = 0

ans = []
for i in range(n):
  if x[i] == '1':
    if cnt1 == 1:
      print(0)
      continue
    cntx = cnt1-1
    mod = ( x10mod_m - pow(2,n-1-i,cntx) ) % cntx
  else:
    cntx = cnt1+1
    mod = ( x10mod_p + pow(2,n-1-i,cntx) ) % cntx
    
  cnt = 1
  mod = format(mod, 'b')
  
  while True:
    if mod == '0':
      break
    mod = format( int(mod,2) % mod.count('1'), 'b')
    cnt += 1
  print(cnt)