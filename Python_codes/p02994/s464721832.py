N, L = [int(n) for n in input().split()]

total = (2*L + N - 1) * N / 2
app = [L + i -1 for i in range(1, N+1)]
app_ = [abs(n) for n in app]
idx = app_.index(min(app_))

print(int(total - app[idx]))