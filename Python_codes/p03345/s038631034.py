'''
Created on 2020/08/17

@author: harurun
'''

import sys
pin=sys.stdin.readline
pout=sys.stdout.write
perr=sys.stderr.write

mod=1000000000000000000
A,B,C,K=map(int,pin().split())
if abs(A-B)>mod:
  print("Unfair")
elif K%2==0:
  print(A-B)
else:
  print(B-A)
