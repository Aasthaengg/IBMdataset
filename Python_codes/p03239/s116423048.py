# 初期入力
from bisect import bisect_right
import sys
input = sys.stdin.readline  #文字列では使わない
N,T = (int(i) for i in input().split())
cost_time =[]
time =[]
for i in range(N):
    c,t = (int(j) for j in input().split())
    cost_time.append((c,t))
    time.append(t)


time.sort()
ind =bisect_right(time,T)
if ind ==0:
    ans ="TLE"
else:
    cost_time.sort(key =lambda x:x[1])
    ans1 =[]
    for i in range(ind):
        ans1.append(cost_time[i][0])
    ans =min(ans1)    
print(ans)