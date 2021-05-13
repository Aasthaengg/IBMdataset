N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = N * T # 総和
cur = 0 # いつまで出るか
for i in range(N):
    if cur > t[i]:
        ans -= cur - t[i]
    cur = t[i] + T
print(ans)