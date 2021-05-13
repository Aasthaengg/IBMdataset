# ans = 売る可能性がある場所の数 = 売って利益が最大値になる可能性がある場所
# Tは関係ない

N,T=map(int,input().split())
A=list(map(int,input().split()))

# 売る場所を一つず右にずらす
# それより前の場所の最安値を持っておく
# 差分のmaxvalを満たす回数をカウント、maxvalが更新されたら回数は1に戻す

INF=10**9+1
maxval=0
minval=INF
ans=0
for i in range(1,len(A)):
  minval=min(A[i-1],minval)
  diff=A[i]-minval
  if diff>maxval:
    maxval=diff
    ans=1
  elif diff==maxval:
    ans+=1

print(ans)
