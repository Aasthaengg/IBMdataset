ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
def z_algo(s):
    ret = [0]*(len(s))
    ret[0] = len(s)
    i = 1
    j = 0
    while i<len(s):
        while i+j<len(s)  and s[i+j]==s[j]:
            j+=1
        ret[i] = j
        if j==0:
            i+=1
            continue
        k=1
        while i+k<len(s) and k+ret[k] <j:
            ret[i+k] = ret[k]
            k+=1
        i+=k
        j=min(ret[k],j-k) ## j= j-kでもよい
    return ret

n = ni()
s = input()
ans = 0
for i in range(n):
    z = z_algo(s[i:])
    for j in range(len(z)):
        if j>=z[j]:
            ans = max(ans,z[j])
print(ans)
