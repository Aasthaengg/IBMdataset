ABC=list(map(int,input().split()))
ABC.sort()
mn=ABC[0]
md=ABC[1]
mx=ABC[2]
if (mx*2-md-mn)%2==0:
  print((mx*2-md-mn)//2)
else:
  print((mx*2-md-mn+3)//2)
