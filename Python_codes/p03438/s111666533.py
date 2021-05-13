# a = 1,2,3
# b = 5,2,2
# 一度の操作でaは2、bは1増える
# b-aが1縮まる
# (bの合計 - aの合計)　が操作回数となる
# (bi - ai) を2で割って切り上げた数(=1を足して2で割って切り捨て)の累計が、必要な操作回数
# (ai - bi) の累計が、必要な操作回数
# この大きいほうが操作回数以下であればYes、なければNo

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

maxope=0
aope=0
bope=0
for i in range(N):
  maxope += B[i] - A[i]
  if B[i] > A[i]:
    aope += (B[i] - A[i] + 1) // 2
  elif A[i] > B[i]:
    bope += A[i] - B[i]

print(("No","Yes")[max(aope,bope) <= maxope])
