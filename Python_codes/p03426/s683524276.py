#!/usr/bin/env python3
import sys
input = sys.stdin.readline
h,w,d = map(int,input().split())
ans = 0
x = [0]*(h*w+1)
y = [0]*(h*w+1)
for i in range(h):
    a = list(map(int,input().split()))
    for j in range(w):
        x[a[j]] = j
        y[a[j]] = i
q = int(input())
#飛び飛びの累積和をとる　視点と
cum_sum_d = [0]*(h*w+1)
for i in range(d,h*w+1):
    cum_sum_d[i] =  cum_sum_d[i-d] + abs(x[i]-x[i-d])+abs(y[i]-y[i-d])
for i in range(q):
    l,r = map(int,input().split())
    ans = cum_sum_d[r] - cum_sum_d[l]
    
    """ #TLE解
    for i in range((r-l)//d): 
        ans += abs(x[l+d*i]-x[l+d*(i+1)])+abs(y[l+d*i]-y[l+d*(i+1)])
        """
    print(ans)