from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
import random
J=998244353
from collections import deque
########################################################
n,x=INPUT()
A=[]
for i in range(n):
    A.append(int(input()))
A.sort()
print(n+(x-sum(A))//A[0])
