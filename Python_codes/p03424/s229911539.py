a=int(input())
b=list(map(str,input().split()))
n=len(set(b))

if n==3:
  print('Three')
else:
  print('Four')