a=[int(input()) for i in range(5)]
k=int(input())
x=max(a)-min(a)
if x<=k:
  print('Yay!')
else:
  print(':(')
