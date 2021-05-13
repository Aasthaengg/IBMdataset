# 歩く部分は連結。左から右としてよい。
# 結局ワープも左から右としてよい。

N,A,B=map(int,input().split())
X = [int(x) for x in input().split()]

ans = 0
for a,b in zip(X[:-1],X[1:]):
  ans += min((b-a)*A,B)
  
print(ans)
