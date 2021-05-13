n,k = map(int,input().split())
h = [int(input()) for H in range(n)]
h.sort()
num,ans = k-1,10**9+1
for i in range(n-num):
  ans = min(ans,(h[i+num]-h[i]))
print(ans)