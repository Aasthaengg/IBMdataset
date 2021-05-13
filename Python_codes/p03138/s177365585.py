n, k = map(int, input().split())
a = list(map(int, input().split()))
keta_a = [0]*41
bin_k = format(k, 'b').zfill(41)
for i in a:
  bin_a = str(format(i, 'b'))
  for j in range(len(bin_a)):
    if bin_a[-j-1] == '1':
      keta_a[-j-1]+=1
dp = [[0]*2 for _ in range(41)] #dp[i桁目まで決めた][smaller flag(0ならKと同じ, 1ならKより小さいことが確定)]
flag = True
for i in range(1, 41):
  if flag:
    if bin_k[i] == '0':
      dp[i][0] = dp[i-1][0]+2**(40-i)*keta_a[i]
    if bin_k[i] == '1':
      flag = False
      dp[i][0] = dp[i-1][0]+2**(40-i)*(n-keta_a[i])
      dp[i][1] = dp[i-1][0]+2**(40-i)*keta_a[i]
  else:
    if bin_k[i] == '0':
      dp[i][0] = dp[i-1][0]+2**(40-i)*keta_a[i]
      dp[i][1] = dp[i-1][1] + 2**(40-i)*max(n-keta_a[i], keta_a[i])
    if bin_k[i] == '1':
      dp[i][0] = dp[i-1][0] + 2**(40-i)*(n-keta_a[i])
      dp[i][1] = max(dp[i-1][0] + 2**(40-i)*(keta_a[i]),dp[i-1][1] + 2**(40-i)*max(n-keta_a[i], keta_a[i]))
print(max(dp[40][0], dp[40][1]))