import sys
input = sys.stdin.readline
from collections import *

N, K = map(int, input().split())
ans = (N//K)**3

if K%2==0:
    c = (N-K//2)//K+1
    ans += c**3

print(ans)