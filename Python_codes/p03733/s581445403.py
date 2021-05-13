n, t = map(int,input().split())
time = list(map(int,input().split()))

ans = 0
wait = 0
for i in range(n):
    if i == 0:
        ans += t
        wait += t
    if wait <= time[i]:
        ans += t
        wait = time[i] + t
    else:
        c = (wait - time[i])
        ans -= c
        ans += t
        wait = time[i] + t

print(ans)