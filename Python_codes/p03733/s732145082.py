n,t = map(int, input().split())
l = list(map(int, input().split()))

ans = t
for i in range(1,n):
  dif = 0 if l[i]-l[i-1] >= t else t-(l[i]-l[i-1])
  ans += (t-dif)
print(ans)