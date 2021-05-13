# -*- coding: utf-8 -*-

def check(T, i, j):
    tmp=[]
    for t in range(i,j):
        tmp.append(T[t])
    print(tmp)

N,C,K =map(int, input().split())
tmp = []
for i in range(N):
    tmp.append(int(input()))

T = sorted(tmp)

ans = i = 0
while i < N:
    start = T[i]
    num = 0
    for j in range(i+1, N):
        num += 1
        if T[j] - start > K or num == C:
            #check(T, i, j)
            i = j
            ans += 1
            break
    else:
        ans += 1
        break

print(ans)