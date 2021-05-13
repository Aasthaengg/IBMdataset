# -*- coding: utf-8 -*-
import sys


N = int(input())
print(0)
s = input()

def judge(x):
    print(x)
    l = input()
    if l=='Vacant':
        sys.exit()
    if x%2 == 0:
        if l == s:
            return True
        else:
            return False
    else:
        if l==s:
            return False
        else:
            return True            
    


ok = 0
ng = N-1
while (abs(ok-ng)>1):
    mid = (ok+ng)//2
    if judge(mid):
        ok = mid
    else:
        ng = mid
        
print(N-1)
l = input()