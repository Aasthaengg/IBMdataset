N=int(input())
S=list(input().split())
a=len(set(S))
if a==3:
  print('Three')
else:
  print('Four')