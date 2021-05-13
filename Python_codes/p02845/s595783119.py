n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7
see = [0 for i in range(n)]
ans = 1
for i in range(n):
  x = a[i]
  if x == 0:
    ans = ans*(3-see[x])%mod
  else:
    ans = ans*(see[x-1]-see[x])%mod
  see[x]+=1
print(ans)