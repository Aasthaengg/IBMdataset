N, L = map(int, input().split())
t = (N-1)*N // 2 + L * N
if L >= 0:
    t -= L
elif -(N-1) < L < 0:
    pass
else:
    t -= L + N - 1

print(t)


