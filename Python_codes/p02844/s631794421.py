import sys
input = sys.stdin.readline
from collections import *

N = int(input())
S = input()[:-1]
ans = 0

for i in range(1000):
    s = '0'*(3-len(str(i)))+str(i)
    now = 0
    
    for j in range(N):
        if S[j]==s[now]:
            now += 1
    
            if now==3:
                break
    
    if now==3:
        ans += 1

print(ans)