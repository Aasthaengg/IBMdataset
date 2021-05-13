# coding: utf-8
import bisect
import math
N, c, k = map(int,input().split())
T = []
for i in range(N):
    T.append(int(input()))
T.sort()
i=0
#print(T)
ans = 0
while True:
    t=bisect.bisect_right(T, T[i]+k)
    #print("i="+str(i))
    if t >= i+c:
        i += c
    else:
        i = t
    ans += 1
    #print(i, ans)
    if i >= N:
        break
print(ans)