N,A,B = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
ans = 0
for i in range(1,N):
    ans += min(abs(X[i]-X[i-1])*A,B)
print(ans)