ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq

s = input()
l = len(s)
k = ni()
def aind(w):
    if w=="a":
        ret = 0
    else:
        ret = 26 - (ord(w) - ord("a"))
    return ret
ans = []
for i in range(l-1):
    if aind(s[i]) <=k:
        ans.append("a")
        k-=aind(s[i])
    else:
        ans.append(s[i])

idx =(ord(s[-1]) - ord("a") +k%26)%26 +ord("a")
ans.append( chr(idx) )
print("".join(ans))
