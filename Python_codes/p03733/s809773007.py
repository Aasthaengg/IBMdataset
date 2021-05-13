N, T = map(int, input().split())
t = list(map(int, input().split()))

t.append(10**10)
total = 0
for i in range(N):
    if t[i+1] - t[i] <= T:
        total += t[i+1] - t[i]
    else:
        total += T
print(total)