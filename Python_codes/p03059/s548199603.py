import itertools
import decimal
import math
import collections
import sys
input = sys.stdin.readline

A,B,T=map(int,input().split())

ans=B*(int(T/A))

print(ans)