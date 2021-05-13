# -*- coding: utf-8 -*-

N = int(input().strip())
K = int(input().strip())
#-----

num=1
for i in range(N):
  if num*2 <= (num + K):
    num *= 2
  else:
    num += K
  
print( num )
