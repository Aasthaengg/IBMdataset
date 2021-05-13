from bisect import bisect_left,bisect
 
n = int(input())
cou = [0 for i in range(n+1)]
for i in range(n):
    now = int(input())
    cou[now] = cou[now-1] + 1  

print(n-max(cou))