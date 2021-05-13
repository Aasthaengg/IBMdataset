ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
ceil = math.ceil

n = ni()
def divisor(n):
    d = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            d.append(i)
            if i != n//i:
                d.append(n//i)
    #d.sort()
    return d

d = divisor(n)
ans = 0
for num in d:
    if num>1 and n%(num-1)==n//(num-1):
        ans+=num-1
print(ans)
