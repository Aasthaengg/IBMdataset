D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(D)]
t = [int(input()) for i in range(D)]
cnt = [0]*26
ans = 0
for i in range(D):
  ans += s[i][t[i]-1]
  cnt[t[i]-1] = i+1
  for j in range(26):
     ans -= c[j] * (i+1-cnt[j])
  print(ans)