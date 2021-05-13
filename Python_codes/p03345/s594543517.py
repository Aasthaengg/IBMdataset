A, B, C, K = map(int, input().split())

x = B-A

if(K%2!=0):
    print(x if x < 10**18 else "Unfair")
else:
    print(-x if (-x < 10**18) else "Unfair" )