N,K,S = map(int, open(0).read().split())
if S < 1000000000:
    ans = ([S]*K) + ([S+1]*(N-K))
    print(*ans)
else:
    ans = ([S]*K) + ([1]*(N-K))
    print(*ans)