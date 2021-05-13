#!/usr/bin/env python3
n = int(input())
s = input()
white = sum([1 for i in s if i == "."])
ans = white#全部黒にするとき
l = 0 # i までのwhiteの数
for i in range(n):
    if s[i] == ".": l += 1
    #print(ans,i+white-2*l)
    ans = min(ans,i+1+white-2*l)
print(ans)