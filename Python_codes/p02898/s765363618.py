from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
import math
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
MOD=10**9+7
import random
#####################################
n,k=INPUT()
A=INPUT()
ans=0
for i in A:
    if i>=k:
        ans+=1
print(ans)
