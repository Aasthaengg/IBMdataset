#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

def f(n):
    ans = 0 
    while n%2 == 0:
        n //= 2
        ans += 1
    return ans 

ans = 0 
for i in a:
    ans += f(i)

print(ans)
