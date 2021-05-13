n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7

cnt = [0]*(n+1)
cnt[0] = 3

ans = 1
for aa in a:
  ans *= cnt[aa]
  ans %= mod
  cnt[aa] -= 1
  cnt[aa+1] += 1
  
print(ans)