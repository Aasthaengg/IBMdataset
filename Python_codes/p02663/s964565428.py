import itertools
import decimal
import math
import collections
import sys
input = sys.stdin.readline

H1,M1,H2,M2,K=map(int,input().split())

ans= H2*60+M2 - (H1 * 60 + M1)
if(ans < 0):
    ans=ans+24*60

print(ans-K)
