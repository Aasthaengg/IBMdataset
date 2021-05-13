N,A,B,*X = map(int, open(0).read().split())
ans = 0
for i in range(N-1):
    ans += min(A*(X[i+1]-X[i]),B)
print(ans)