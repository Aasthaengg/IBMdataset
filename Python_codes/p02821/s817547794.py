import bisect

N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
#print(A)

# Aの累積和を求めておく。
csum = [A[0] for _ in range(N+1)]
for i in range(1,N):
  csum[i] = csum[i-1]+A[i]

# M回以上握手できるとなる最小の幸福度を求める。
# l:幸福度l以上となる握手がMパターン以上存在する。
# r:幸福度r以上となる握手がMパターン以上存在しない。
l = 0
r = 10**6
while (l+1 < r):
  m = (l+r)//2
  p = 0 # 幸福度がm以上になる握手の回数
  for a in A:
    q = bisect.bisect_left(A,m-a)
    #print(q,m-a,A)
    p += N-q
  #print(l,m,r,p)
  if p >= M:
    l = m
  else:
    r = m
#print(l,m,r)

# 幸福度がl-1のときに握手ができる回数と幸福度を求める。
# その回数とMとの差の回数だけ、幸福度にlを追加する。
# (幸福度がlになる握手のパターンは複数ある可能性がある)
ans = 0
cnt = 0
for a in A:
  q = bisect.bisect_right(A,l-1-a)
  if q == 0:
    ans += csum[N-1]+a*N
  elif q < N:
    ans += csum[N-1]-csum[q-1]+a*(N-q)
  cnt += N-q
  #print(a,q,ans,cnt)
ans += l*(M-cnt)
print(ans)
