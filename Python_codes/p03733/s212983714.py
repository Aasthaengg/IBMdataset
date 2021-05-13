N,T = map(int,input().split())
L = list(map(int,input().split())) 

ans = 0
end = 0
for i in range(N):
  ans += min(L[i]+T-end,T)
  end = L[i] + T
print(ans)
