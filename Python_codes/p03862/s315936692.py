from sys import stdin
import collections
import math


n,x   = [int(x) for x in stdin.readline().rstrip().split()]
arr = [int(x) for x in stdin.readline().rstrip().split()]

ans = 0
if arr[0] > x :
    ans += arr[0] - x 
    arr[0] = x
for i in range(0,n-1):
    s = arr[i] + arr[i+1]
    if s > x :
        d = s-x
        arr[i+1] -= s - x
        ans += d

print(ans)