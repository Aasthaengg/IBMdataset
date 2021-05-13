_, D, X, *A = map(int, open(0).read().split())

ans = X
for a in A:
    ans += (D + a - 1) // a
print(ans)
