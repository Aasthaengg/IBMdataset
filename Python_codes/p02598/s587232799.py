from math import ceil
N,K = map(int,input().split())
A = list(map(int,input().split()))

def is_ok(X):
    #最大値をX以下にできるか
    cnt = 0
    for a in A:
        cnt += ceil(a/X)-1
    return cnt <= K

def bisearch(high,low):
    while high - low > 1:
        mid = (high+low)//2
        if is_ok(mid):
            high = mid
        else:
            low = mid
    return high

print(bisearch(10**9+1,0))