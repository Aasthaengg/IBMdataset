N, A, B = map(int, input().split())
X = list(map(int, input().split()))
here = X.pop(0) 
ans = 0

for _ in range(N-1):
    walk = (X[0] - here) * A
    if walk > B:
        ans += B
    else:
        ans += walk
    here = X.pop(0)

print(ans)