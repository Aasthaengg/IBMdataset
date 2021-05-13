import math
import collections
from operator import mul
from functools import reduce
import bisect
import string

numbers = "0123456789"
alphabets = string.ascii_letters # a-z+A-Zをロード
characters = numbers + alphabets
def base_cvt(value, n=2):
    try:
        tmp = int(value)
    except:
        raise ValueError('Invalid value:', value)
 
    if n < 2 or n > len(characters):
        raise ValueError('Invalid n:', value)
    result = ''
    tmp = int(value)
    while tmp >= n:
        idx = tmp%n
        result = characters[idx] + result
        tmp = int(tmp / n)
    idx = tmp%n
    result = characters[idx] + result
    return result

n,a,b,c=map(int,input().split())
l=[0]*n
for i in range(n):
    l[i]=int(input())

def zeropad(s,i):
    while len(s)<i:
        s="0"+s
    return s


mp=10000000000000000
for i in range(4**n):
    A=0
    B=0
    C=0
    ai=0
    bi=0
    ci=0
    s=base_cvt(str(i),4)
    s=zeropad(s,n)
    for j in range(n):
        if s[j]=='1':
            A+=l[j]
            ai+=1
        elif s[j]=='2':
            B+=l[j]
            bi+=1
        elif s[j]=='3':
            C+=l[j]
            ci+=1
    if ai>0 and bi>0 and ci>0:
        mp=min(mp,10*((ai-1)+(bi-1)+(ci-1))+abs(A-a)+abs(B-b)+abs(C-c))


print(mp)









