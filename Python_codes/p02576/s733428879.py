N, X, T = map(int, input().split())

time = divmod(N, X)
ans = 0

if time[1] != 0:
    ans = T * (time[0] + 1)
else:
    ans = T * time[0]

print(ans)