A,B=map(int,input().split())

if B==1:print(0)
else:
  n = 1
  for i in range(1,50):
    n += A-1
    if n>=B:break

  print(i)