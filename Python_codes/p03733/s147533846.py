N, T = map(int, input().split())
t = list(map(int, input().split()))

open = [t[0] + T]
ans = T
for n in range(N):
    if n == 0:
        continue
    else:
        if t[n] >= open[-1]:
            ans += T
            open.append(t[n] + T)
        else:
            ans += t[n] - t[n-1]
            open.append(t[n] + T)

print(ans)