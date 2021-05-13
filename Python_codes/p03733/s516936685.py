n, T = map(int, input().split())
t = list(map(int, input().split()))
cum_sub = [0] + [t[i]-t[i-1] for i in range(1,n)]

ans = 0
for each in cum_sub[1:]:
  ans += min(T, each)
  
ans += T
print(ans)