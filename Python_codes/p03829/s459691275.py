N,A,B = list(map(int,input().split()))
X = list(map(int,input().split()))

ans = 0
for s,e in zip(X[:-1],X[1:]):
    ans += min(B,A*(e-s))
print(ans)