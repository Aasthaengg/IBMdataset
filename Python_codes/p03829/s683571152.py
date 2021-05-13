N, A, B = map(int, input().split())
X = list(map(int, input().split()))

nowX = X[0]
ans = 0
for x in X[1:]:
    ans += min((x-nowX)*A, B)
    nowX = x
print(ans)