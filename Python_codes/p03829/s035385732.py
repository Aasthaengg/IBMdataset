N,A,B = map(int,(input().split()))
X = list(map(int,(input().split())))
ans = 0
now = X[0]
for i in range(1,N):
    if (X[i]-now)*A <= B:
        ans += (X[i]-now)*A
    else:
        ans += B
    now = X[i]
print(ans)