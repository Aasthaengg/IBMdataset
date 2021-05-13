import sys
input = sys.stdin.readline
from collections import *

S = input()[:-1]

if S=='keyence':
    print('YES')
    exit()

for i in range(len(S)):
    for j in range(i, len(S)):
        T = S[:i]+S[j+1:]
        
        if T=='keyence':
            print('YES')
            exit()

print('NO')