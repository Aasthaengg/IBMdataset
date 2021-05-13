N, A, B, *X = map(int, open(0).read().split())
ans = sum(min((X[i]-X[i-1])*A,B) for i in range(1,N))
print(ans)