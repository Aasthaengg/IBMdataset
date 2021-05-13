N,K = map(int, input().split())
a = list(map(int, input().split()))
Kbin = bin(K)[2:]
Kbin = Kbin.zfill(43)
s = len(str(K))
sbin = len(Kbin)
bintbl1 = [0 for i in range(sbin)]
bintbl0 = [0 for i in range(sbin)]
for i in range(N):
  abin = bin(a[i])[2:]
  abin = abin.zfill(sbin)
  for j in range(sbin):
    if abin[j] == "1":
      bintbl1[j] += 1
    else:
      bintbl0[j] += 1
DP = [[[0 for i in range(2)] for j in range(2)] for k in range(sbin)]
for i in range(1,sbin):
  if Kbin[i] == "1":
    if sbin-len(bin(K)[2:]) == i:
      DP[i][1][0] = max(DP[i-1][0][0],DP[i-1][1][0]) + bintbl0[i]*2**(sbin-i-1)
      DP[i][0][1] = max(DP[i-1][0][0],DP[i-1][0][1],DP[i-1][1][1],DP[i-1][1][0]) + (bintbl1[i]*2**(sbin-i-1))
    else:
      DP[i][1][0] = max(DP[i-1][0][0],DP[i-1][1][0]) + bintbl0[i]*2**(sbin-i-1)
      DP[i][1][1] = max(DP[i-1][0][1],DP[i-1][1][1]) + bintbl0[i]*2**(sbin-i-1)
      DP[i][0][0] = 0
      DP[i][0][1] = max(DP[i-1][0][0],DP[i-1][0][1],DP[i-1][1][1],DP[i-1][1][0]) + (bintbl1[i]*2**(sbin-i-1))
  if Kbin[i] == "0":
    if sbin-len(bin(K)[2:])>i:
      DP[i][0][0] = max(DP[i-1][0][0],DP[i-1][1][0]) + bintbl1[i]*2**(sbin-i-1)
    else:
      DP[i][1][0] = 0
      DP[i][1][1] = max(DP[i-1][0][1],DP[i-1][1][1]) + bintbl0[i]*2**(sbin-i-1)
      DP[i][0][0] = max(DP[i-1][0][0],DP[i-1][1][0]) + bintbl1[i]*2**(sbin-i-1)
      DP[i][0][1] = max(DP[i-1][0][1],DP[i-1][1][1]) + bintbl1[i]*2**(sbin-i-1)
print(max(DP[sbin-1][0][0],DP[sbin-1][0][1],DP[sbin-1][1][0],DP[sbin-1][1][1]))