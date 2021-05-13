import math

_=list(map(int,input().split()))
n,k=_[0],_[1]
W=[]
for i in range(n):
    W.append(int(input()))

def n_cal(num_track,weights,threshold):
    numbers_=0
    for i in range(num_track): #each tracktor
        sum_=0
        while sum_<=threshold and numbers_<=len(weights)-1: #each tracktor's capacity
            sum_+=weights[numbers_] #each tracktor's weight
            if sum_<=threshold:numbers_+=1
            else:pass
    return numbers_

minimum_=max(W)
maximum_=sum(W)
P=range(minimum_,maximum_+1)

left=0;right=len(P)
mid=math.floor((left+right)/2)
while left<right:
    if n_cal(k,W,P[mid])<n:
        left=mid+1
    elif n==n_cal(k,W,P[mid]) and n==n_cal(k,W,P[mid-1]):
        right=mid
    else:break
    mid=math.floor((left+right)/2)
print(P[mid])
