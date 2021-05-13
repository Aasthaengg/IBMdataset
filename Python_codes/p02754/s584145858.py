N, A, B = map(int, input().split())

pair = N // (A + B)
remain = N % (A + B)

print(A * pair + min(remain, A))
