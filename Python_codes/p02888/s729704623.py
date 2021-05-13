from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
import math
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math as M
MOD=10**9+7
import bisect
#####################################
n=int(input())
A=INPUT()
A.sort()
ans=0
for i in range(n):
    for j in range(i+1,n):
        ans+=bisect.bisect_left(A,A[i]+A[j],0,n)-1-j
print(ans)
