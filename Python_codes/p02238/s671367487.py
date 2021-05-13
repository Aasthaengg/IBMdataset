from __future__ import division,print_function
import time
import sys
import io
import re
import math
start = time.clock()
i = 0
def walk(index,tm,L,d,f):
    tm+=1
    d[index]=tm
    for i in L[index]:
        if not d[i-1]:
            tm=walk(i-1,tm,L,d,f)
    tm+=1
    f[index]=tm
    return tm
 
def main():
    num=int(sys.stdin.readline())
    L=[]
    for _ in range(num):
        L.append([int(s) for s in sys.stdin.readline().split()[2:]])
    d=[0]*num
    f=[0]*num
    tm=0
    for i in range(num):
        if not d[i]:
            tm=walk(i,tm,L,d,f)
    for i in range(num):
        print(i+1,d[i],f[i])
 
main()