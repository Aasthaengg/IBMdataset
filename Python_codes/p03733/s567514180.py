N, T = tuple(map(int, input().split()))
t = list(map(int, input().split()))
if N == 1:
    print(T)
    exit()

total = 0
for i in range(N-1):
    total += min(t[i+1] - t[i], T)
total += T
print(total)