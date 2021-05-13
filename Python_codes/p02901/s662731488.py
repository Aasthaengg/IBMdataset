n,m = map(int,input().split())
dp = [0]+[10**8+10]*(2**n-1)
#len(dp)==16　（2**n）　扉の開閉状態
#dp: その開閉状態を実現するための鍵の値段の最小値

#それぞれの鍵について
for i in range(m):
  a,b = map(int,input().split())
  #x: 開く扉の番号
  #2**(1-1)==000000000001   2**(12-1)==100000000000
  #sは　100010111000みたいなやつ（その鍵で開く扉が１）
  s = sum([2**(x-1) for x in list(map(int,input().split()))])
  for j in range(2**n):
    #| : or
    #（ある状態＋その鍵を使って開けられるやつ）の状態　　もともとの数値か、鍵を使うか
    dp[j|s] = min(dp[j|s],dp[j]+a)
if dp[-1] <= 10**8:
  print(dp[-1])
else:
  print(-1)

