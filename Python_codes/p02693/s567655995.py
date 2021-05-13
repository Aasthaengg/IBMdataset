K = int(input())
A,B = map(int,input().split())

amari =int(B/K)
if A<=K*amari and K*amari<=B:
  print('OK')
else :
  print('NG')