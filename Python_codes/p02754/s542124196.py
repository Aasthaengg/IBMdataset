H, A, B = map(int, input().split())
p = H // (A + B)
q = H % (A + B)
ans = p * A
if q >= A:
    ans += A
else:
    ans += q
print(ans)