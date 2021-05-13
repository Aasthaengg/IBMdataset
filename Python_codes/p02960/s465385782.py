S = str(input()); N = len(S)
S = list(S); S.reverse() #1桁目からに変換
MOD = pow(10,9)+7
dp = [0 for _ in range(13)] #13で割ってi余る個数
dp[0] = 1
keta = 1
for i in range(N):
  p = [0 for _ in range(13)]
  dp,p = p,dp #dpが次。pが一個前。
  if i != 0:
    keta = (keta*10)%13
  if S[i] == "?":
    for x in range(10):
      amari = x*keta%13
      for j in range(13):
        if j >= amari:
          mae = j-amari
        else:
          mae = j-amari+13
        dp[j] += p[mae]%MOD
  else:
    amari = int(S[i])*keta%13
    for j in range(13):
      if j >= amari:
        mae = j-amari
      else:
        mae = j-amari+13
      dp[j] += p[mae]%MOD
#print(dp)
print(dp[5]%MOD)