import sys
def input(): return sys.stdin.readline().strip()

def resolve():
   s=list(input())
   from collections import Counter
   c=Counter(s)# ()にカウンターの対象のリストの変数名
   x=c['a']
   y=c['b']
   z=c['c']
   if (x-1)*2<=y+z and (y-1)*2<=x+z and (z-1)*2<=x+y:
       print('YES')
   else:
       print('NO')

resolve()