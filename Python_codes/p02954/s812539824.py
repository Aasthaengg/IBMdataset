import sys
input=sys.stdin.readline
from math import ceil

s=input().rstrip()
s=s.replace("LR","L,R")
s=s.split(",")
ans=[]
for block in s:
    R=block.count("R")
    L=block.count("L")
    left=ceil(R/2)+(L//2)
    right=(R//2)+ceil(L/2)
    for i in range(R-1):
        ans.append(0)
    ans.append(left)
    ans.append(right)
    for i in range(L-1):
        ans.append(0)
print(*ans)