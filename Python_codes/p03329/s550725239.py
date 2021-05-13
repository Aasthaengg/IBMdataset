import math,numpy, collections

n = int(input())
ans = n
cnt = 0
for i in range(n+1):
    cnt = 0
    x = i
    while x >0:
        cnt += x%6
        x = x//6
    y = n-i
    while y >0:
        cnt += y%9
        y = y//9
    ans = min(ans,cnt)

print(ans)