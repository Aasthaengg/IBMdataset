N,T = map(int, input().split())
time = [int(t) for t in input().split()]

ans = T
for i in range(1, N):
    if time[i-1]+T <= time[i]:
        ans += T
    else:
        ans += time[i]-time[i-1]

print(ans)