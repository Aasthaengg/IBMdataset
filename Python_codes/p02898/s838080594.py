N, K = map(int, input().split())
x = list(map(int, input().split()))
total = 0
for i in range(N):
    if x[i] >= K:
        total = total + 1
    else:
        total = total + 0
print(total)