import math

def count(N,K,mid,a):
    cnt = 0
    for i in range(N):
        cnt += math.ceil(a[i]/mid-1)
    if cnt > K:
        return False
    else:
        return True

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    low = 1
    high = 10**9+1
    mid = (low+high)//2

    while high > low+1:
        if count(N,K,mid,a):
            high = mid
        else:
            low = mid
        mid = (low+high)//2
    
    if count(N,K,low,a):
        print(low)
    else:
        print(high)

main()