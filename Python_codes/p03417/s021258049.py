N, M = map(int, input().split())
answer = 0

if N == 1 and M == 1:
    answer = 1
elif N == 1 or M == 1:
    answer = max(N, M)-2
else:
    answer = (N-2)*(M-2)

print(answer)
