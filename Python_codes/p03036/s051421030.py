import math
import time
from collections import defaultdict, deque
from sys import stdin, stdout
from bisect import bisect_left, bisect_right
r,d,x=map(int,stdin.readline().split())
ans=x 
for _ in range(10):
    ans=(r*ans)-d 
    print(ans)