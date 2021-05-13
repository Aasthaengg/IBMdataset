from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
INT_MIN=-10**13
import bisect as B
###############################################################################\
n,m=INPUT()
A=INPUT()
A.sort()
for _ in range(m):
    B.insort(A,A.pop()//2)
print(sum(A))
