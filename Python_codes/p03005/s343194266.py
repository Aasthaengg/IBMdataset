#標準入力
N,K = (int(x) for x in input().split())
ans = 0
ans = N-K
if K==1:
  ans=0
print(ans)

