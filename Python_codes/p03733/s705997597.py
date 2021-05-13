N, T = map(int, input().split())
time = list(map(int, input().split()))
syawaend = 0
ans = 0
for i in range(N):
  if syawaend <= time[i]:
    syawaend = time[i]+T
    ans += T
  else:
    syawaend = time[i]+T
    ans += time[i]-time[i-1]
print(ans)
