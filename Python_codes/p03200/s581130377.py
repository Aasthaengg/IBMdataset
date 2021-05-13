# -*- coding:utf-8 -*-
S = list(input())

cnt_b = 0 
ans = 0

for i in range(len(S)):
    if S[i] == "B":
        cnt_b += 1
    if S[i] == "W":
        ans += cnt_b
print(ans)        