# coding: utf-8
import math
#a, d = map(int,input().split())
N = int(input())
S = input()
ans = 0
x = 0
for i in range(N):
    if S[i] == "I":
        x += 1
    elif S[i] == "D":
        x -= 1
    ans = max(ans, x)

print(ans)