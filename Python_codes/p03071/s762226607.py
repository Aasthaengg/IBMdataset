A, B = map(int, input().split())

ans = 0
if A >= B:
    ans += A
    A -= 1
else:
    ans += B
    B -= 1

print(ans + max(A, B))
