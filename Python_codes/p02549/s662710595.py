#coding: UTF-8

N, K = map(int, input().split())
mod = 998244353
s = []
for k in range(K):
  s.append(list(map(int,input().split())))
#print(s)
cnt = [0]*N
cnt[0] = 1
sum = [0]*N
sum[0] = 1
for i in range(1,N):
  for j in range(K):
    #j個目の区間について
    if i > s[j][1]: #後ろのほう
      cnt[i] += sum[i-s[j][0]] - sum[i-s[j][1]-1]
    elif i >= s[j][0]:
      cnt[i] += sum[i-s[j][0]]
    cnt[i] = cnt[i] % mod
    sum[i] = (sum[i-1] + cnt[i])% mod
print(cnt[-1] % mod)
