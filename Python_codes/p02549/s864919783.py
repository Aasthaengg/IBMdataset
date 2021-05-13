import numpy as np

m = 998244353
N, K = map(int, input().split())
span = []
for K in range(K):
    l , r = map(int, input().split())
    span.append([l, r])

add = [0,1]# 累積和
ans = [1]

for i in range(2,N+1):
    tmp = 0
    for s in span:
        l, r = s[0], s[1]+1
        if l > len(ans):
            continue
        elif r >= len(ans)+1:
            r = len(ans)+1
        tmp += (add[i-l] - add[i-r])%m
    ans.append(tmp%m)
    add.append(add[-1]+tmp)

print(ans[-1]%m)