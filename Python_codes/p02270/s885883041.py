# -*- coding: utf-8 -*-
N, k = [int(n) for n in input().split()]
W = []

def search(W, k, P):
    tmp = 0
    track = 1
    for w in W:
        if tmp + w <= P:
            tmp += w
        else:
            track += 1
            tmp = w
    if track > k:
        return False
    else:
        return True         
        

for n in range(N):
    W.append(int(input()))

left = max(sum(W) // N, max(W))
right = sum(W)

while right - left > 1 :
    mid = (left + right)//2
    if search(W, k, mid):
        right = mid
    else:
        left = mid
    
if search(W, k, left):
    print(left)
else:
    print(right)  