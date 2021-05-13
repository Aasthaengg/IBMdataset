X,Y = map(int, input().split())

K = Y*0.5-X
T = 2*X - Y*0.5

if 0<= T and T == T//1 and 0<= K and K == K//1:
  print('Yes')
else:
  print('No')
