import sys
import collections
import copy
def input(): return sys.stdin.readline().strip()
A,B,C= map(int,input().split())
if (B-A) == (C-B):
    print("YES")
else:
    print("NO")
