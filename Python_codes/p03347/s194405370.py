#!usr/bin/env python3

# A
"""
a,b,c,k = map(int ,input().split())
s = b-a
if (k%2 == 0):
    s *= -1
print(s)
"""
# B
# C
n = int(input())
a = [int(input()) for i in range(n)]
if a[0] != 0:
    print(-1)
    quit()
for i in range(1,n):
    if a[i] > i:
        print(-1)
        quit()
    if a[i]-a[i-1] > 1:
        print(-1)
        quit()
ans = a[-1]
for i in range(n-1)[::-1]:
    if a[i]+1 == a[i+1]:continue
    ans += a[i]
print(ans)


# D

# E

# F
