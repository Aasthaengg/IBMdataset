import sys
from collections import deque
sys.setrecursionlimit(10*5)


n,k=map(int,input().split())
ans=n-k+1
print(ans)
