N = int(input())

def digit_sum(A):
    S = 0
    while A > 0:
        S += A % 10
        A //= 10
    return S

ans = 10e+5
for A in range(1, N):
    cand = digit_sum(A) + digit_sum(N - A)
    ans = min(ans, cand)

print(ans)