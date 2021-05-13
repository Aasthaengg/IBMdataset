import sys,os,math
from collections import Counter, defaultdict, deque
import bisect
from sys import stdin, stdout
from itertools import repeat
import Queue
import time
 
 
# sys.stdin = open('input')
# n, k = map(int, raw_input().split())
# da = map(int, raw_input().split())
# db = map(int, raw_input().split())
 
BT = int(1e9)
def main():
    start = time.time()
    m, k = map(int, raw_input().split())
    if k >= (1<<m):
        print -1
        return
    if m==1 and k==0:
        print 1,1,0,0
        return
    if m==1 and k==1:
        print -1
        return
    ans = []
    for i in range(1<<m):
        if i!=k:
            ans.append(i)
    ans.append(k)
    for i in range((1<<m)-1, -1, -1):
        if i!=k:
            ans.append(i)    
    ans.append(k)
    print ' '.join(map(str, ans))

 
main()