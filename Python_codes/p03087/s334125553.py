N, Q = map(int, input().split())
S = input()

cnt = [0]*N
flag = [0]*N
if S[:2] == 'AC':
  cnt[1] = 1
  flag[1] = 1
  
for i in range(1,N-1):
  if S[i] == 'A' and S[i+1] == 'C':
    cnt[i+1] = cnt[i-1] + 1
    flag[i+1] = 1
  else:
    cnt[i+1] = cnt[i]

for _ in range(Q):
  l, r = map(int, input().split())
  if l == 1:
    print(cnt[r-1])
  else:
    if flag[l-1] == 0:
      print(cnt[r-1]-cnt[l-2])
    else:
      print(cnt[r-1]-cnt[l-2]-1)