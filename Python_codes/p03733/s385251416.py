N, T = map(int, input().split())
t = list(map(int, input().split()))
count = 0
for i in range(1, N):
    m = t[i]-t[i-1]
    if m < T:
        count += m
    else:
        count += T
print(count+T)