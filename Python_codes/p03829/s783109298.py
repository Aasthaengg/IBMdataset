N, A, B = map(int, input().split())
X = [int(i) for i in input().split()]

ans = 0
before = X[0]
for i in X:
    ans += min((i-before)*A, B)
    before = i

print(ans)