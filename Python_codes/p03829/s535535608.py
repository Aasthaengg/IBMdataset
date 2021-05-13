N,A,B = map(int,input().split())

X = list(map(int,input().split()))

ans = 0

for i in range(1,N):
    dis =  X[i] - X[i-1]
    if B >= A * dis:
        ans += A * dis
    else:
        ans += B
print(ans)
