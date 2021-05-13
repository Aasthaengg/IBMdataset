N,K,X,Y = map(int, open(0).read().split())
if N < K:
    ans = N*X
else:
    ans = K*X + (N-K)*Y
print(ans)
