# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

#n,*ta = map(int, read().split())
s = input()
n = len(s)
t = "gp"*((n+2)//2)

ans = 0
for i,j in zip(s,t):
    if i != j:
        if i=="g": ans += 1
        else: ans -= 1

print(ans)