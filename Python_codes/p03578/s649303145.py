n=int(input())
d=list(map(int, input().split()))
m=int(input())
t=list(map(int,input().split()))

d.sort()
t.sort()
flg_no = 0
index_start=0
for i in range(m):
  index=index_start
  flg_fin=0
  while index < n:
    if d[index] == t[i]:
      index_start=index+1
      flg_fin=1
      break
    index+=1
  if flg_fin == 0:
    print('NO')
    flg_no = 1
    break
if flg_no == 0:
  print('YES')