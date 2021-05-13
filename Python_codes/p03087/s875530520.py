N, Q = map(int, input().split())
S = str(input())
li = []
cnt = 0

for i in range(N-1):
  if S[i]=='A' and S[i+1]=='C':
    cnt += 1
    li.append(cnt)
  else:
    li.append(cnt)

for i in range(Q):
  l, r = map(int, input().split())
  if l > 1:
    ans = li[r-2] - li[l-2]
  else:
    ans = li[r-2]
  print(ans)
