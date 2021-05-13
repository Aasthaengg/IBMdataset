n=int(input())
import math
import itertools
zahyou=[[0,0]]
for i in range(n):
    tmp=[int(x) for x in input().split()]
    zahyou.append(tmp)

    ans=0
    
for seq in itertools.permutations(range(1,n+1)):
    dist=0
    for i in range(len(seq)-1):
        dist+=math.sqrt((zahyou[seq[i]][0]-zahyou[seq[i+1]][0])**2+(zahyou[seq[i]][1]-zahyou[seq[i+1]][1])**2)
    ans+=dist

print(ans/math.factorial(n))