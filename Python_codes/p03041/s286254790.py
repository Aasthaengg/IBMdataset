import sys
import math
sys.setrecursionlimit(10**6)
from collections import defaultdict

n,k=map(int,input().split())
s=input()

ans=s[:k-1]+s[k-1].lower()+s[k:]
print(ans)
