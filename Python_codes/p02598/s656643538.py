import copy
import math

def judge(As,K,C):
    count = 0
    for i in range(len(As)):
        if As[i]%C == 0:
            m = As[i]//C - 1
        else:
            m = As[i]//C
        count += m
    if count <= K:
        return True
    else:
        return False

N, K = list(map(int,input().split()))
As = list(map(int,input().split()))

l = 0
r = max(As)
while(r-l>1):
    mid = (l+r)//2
    if judge(As,K,mid):
        r = mid
    else:
        l = mid
print(r)