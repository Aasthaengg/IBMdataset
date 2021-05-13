def Count_car(n,k,S,P):
    storage = 0
    number = 1
    for i in range(n):
        weight = S[i]
        if storage + weight > P:
            storage = weight
            number += 1
        else:
            storage += weight
    if number > k:return 0
    return 1
n,k = list(map(int,input().split()))
total = 0
M = 0
S = []
for _ in range(n):
    number = int(input())
    S.append(number)
import math
P = max(max(S),math.ceil(sum(S)/k))
Q = sum(S)
while True:
    if Q - P <= 1:
        if Count_car(n,k,S,P):
            break
        else:
            P = P+1
            break
    mid = (P+Q)//2
    if Count_car(n,k,S,mid):
        Q = mid
    else:
        P = mid
print(P)
