N, T = map(int, input().split())
A = list(map(int, input().split()))
max_prof = 0
cnt = 0
max_after = [0] * N
max_after[-1] = A[-1]
for i in range(N-1)[::-1]:
    max_after[i] = max(max_after[i+1], A[i])
for i in range(N-1):
    prof = max_after[i+1] - A[i]
    if prof == max_prof:
        cnt += 1
    elif prof > max_prof:
        max_prof = prof
        cnt = 1
print(cnt)
