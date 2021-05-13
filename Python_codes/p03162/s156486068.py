N=int(input())

A=[[0]*3 for i in range(N+1)]
for i in range(N):
  a=list(map(int,input().split()))
  A[i]=a

#ステップ1
dp=[[-float('inf')] * 3 for i in range(N+1)]
#N+1行作っておくことでループを回すときにN日目だけ分けて考える必要がなくなる。

#ステップ2
dp[0]=A[0] #初日にAを実行する日の幸福度は確定している。以下同様。

#ステップ3
for i in range(N):
  for j in range(3): #i+1日目に行うアクティビティ
    for k in range(3): #i+2日目に行うアクティビティ
      if j != k: #2日連続同じアクティビティは禁止
        if dp[i+1][k] < dp[i][j] + A[i+1][k]:
          dp[i+1][k] = dp[i][j] + A[i+1][k]
        
#ステップ4
ans=max(dp[N-1])
print(ans)