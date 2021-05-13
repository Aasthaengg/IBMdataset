n,k=map(int,input().split())
lists=list(map(int,input().split()))

import math
import fractions
flag=True
#最大公約数
def union_gcd(lists):
    if len(lists)==1:
        return lists[0]
    elif len(lists)>1:
        num=lists[0]
        for i in range(1,len(lists)):
            num=fractions.gcd(num,lists[i])
        return num
if k%union_gcd(lists)==0 and k<=max(lists):
    flag=True
else:
    flag=False
if flag:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")