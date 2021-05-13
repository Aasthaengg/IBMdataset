N = int(input())
a = list(map(int,input().split()))

cum = [0]*(N+1)
ans = 10**12
total = sum(a)
for i in range(N):
  cum[i+1] = cum[i] + a[i]
  ans = min(ans,abs(cum[i+1]-(total-cum[i+1])))
print(ans)
