N, A, B = map(int, input().split())

ans = A * (N // (A + B))
if N % (A + B) > A:
    ans += A
else:
    ans += N % (A + B)

print(ans)
