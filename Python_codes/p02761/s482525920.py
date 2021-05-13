N, M = map(int, input().split())
ans='1' + '0'*(N-1) if N>1 else '0'
chk=[False]*N

for m in range(M):
  s, c = input().split()
  s=int(s)
  if s==1 and c=='0' and N>1:
    print(-1); exit(0)
  if chk[s-1] and c!=ans[s-1]:
    print(-1); exit(0)
  chk[s-1]=True
  ans = ans[:s-1] + c + ans[s:]
  #print(chk, ans)
print(ans)