'''
Author : Shubhanshu Jain;
'''
import sys
input = sys.stdin.readline
from collections import Counter
import math
import random;
mod =1000000007
r1 = lambda : int(input());
rm = lambda : map(int,input().split());
rls = lambda : list(rm())

a,b,x = rm();
if(x<a):
    print("NO");
elif((a+b)>=x):
    print("YES");
else:
    print("NO")