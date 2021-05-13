#!/usr/bin/ python3.8
n=int(input())
p=[int(x) for x in input().split()]
ans=0
for i in range(1,n-1):
    if max(p[i - 1], p[i + 1]) > p[i] > min(p[i - 1], p[i + 1]):
        ans += 1
print(ans)
