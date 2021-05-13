# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n,t,*a = map(int,read().split())


ans = 0

s = a[0]
for i in a:
    s = max(i,s)
    ans += i+t-s
    s = i+t

print(ans)