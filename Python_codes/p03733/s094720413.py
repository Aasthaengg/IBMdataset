N,T = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = T
for i in range(1, N):
    ans += T
    if t[i]-t[i-1] < T:
        # 稼働中にスイッチが押されたらオーバーラップ分を引く
        ans -= (t[i-1] + T - t[i])
print(ans)