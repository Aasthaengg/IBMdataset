h,w,a,b = map(int,input().split())
x = '1'*a + '0'*(w-a)
xinv = '0'*a + '1'*(w-a)
for i in range(h):
  row = x if i < b else xinv
  print(row)