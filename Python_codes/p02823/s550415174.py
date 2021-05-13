N, A, B = map(int, input().split())
cnt = 0
if (A + B) % 2:
    if A - 1 < N - B:
        cnt += A
        B = max(1, B - A)
        A = 1
    else:
        cnt += N - B + 1
        A = min(N, A + N - B + 1)
        B = N
print(cnt + B - (A + B) // 2)
