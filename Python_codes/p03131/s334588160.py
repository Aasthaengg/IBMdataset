K,A,B = map(int,input().split())
if A+1 >= B:
    print(K+1)
else:
    if K < A-2:
        print(K+1)
    else:
        K -= A-1
        chance = K//2
        ans = 0
        ans += chance*(B-A)+A
        spare = K%2
        ans += spare
        print(ans)