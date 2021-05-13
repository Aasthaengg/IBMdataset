N, T = map(int,input().split())
t = list(map(int,input().split()))
t.append(t[-1]+T)


ans = 0
for n in range(N):
  ans = ans + min(t[n+1]-t[n],T)
  
print(ans)