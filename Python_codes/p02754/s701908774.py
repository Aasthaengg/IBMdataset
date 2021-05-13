N, A, B = map(int, open(0).read().split())

ans = N // (A+B) * A
x = N % (A+B)
if x >= A:
    ans += A
else:
    ans += x

print(ans)