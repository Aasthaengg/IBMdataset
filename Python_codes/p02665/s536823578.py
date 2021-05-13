n=int(input())
a=list(map(int,input().split()))

# nowは今見てる深さに存在しうる最大の頂点数
# max[i] := 深さiに存在しうる最大の頂点数
# maxが2*10^18超えたら無視してる
now, max = 1, [None] * (n + 1)
for i in range(n + 1):
  if a[i] > now:
    print(-1)
    exit(0)
  max[i] = now
  now = min((now - a[i]) * 2, 2000000000000000000)

# 次にボトムアップ
# upは今見ている深さに対して登ってくる辺数
# 当然だけど、up + a[i]がその深さに存在しうる最大の頂点数
# だから、min(max[i], up + a[i])が深さiに存在しうる最大の頂点数になる
# あとはその和を取る
ans, up = 0, 0
for i in range(n, -1, -1):
  count = min(max[i], up + a[i])
  ans += count
  up = count
print(ans)