k=int(input())
a, b=map(int,input().split())
n=1
while n*k<=1000:
  if n*k>b:
    print('NG')
    break
  elif a<=n*k:
    print('OK')
    break
  else:
    n=n+1