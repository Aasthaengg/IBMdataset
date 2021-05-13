N, L = map(int, input().split())

low = L+1-1
high = L+N-1
total = (low+high)*N//2

min_diff = 10**4
min_total = -1
for i in range(N):
    diff = abs(L+i)
    if diff < min_diff:
        min_diff = diff
        min_total = total - (L+i)
print(min_total)
