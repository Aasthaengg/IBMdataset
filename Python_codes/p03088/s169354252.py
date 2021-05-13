N=int(input())
#含んではいけない
#AGC
#GAC
#ACG
#ACGC
#AGGC
#ATGC
#AGAC
#AGTC

# AAA,AAC,AAG...という3文字セットの組み合わせ64通り
from collections import deque
stack=deque([""])
buf=[]
while stack:
  s=stack.popleft()
  if len(s)==3:
    buf.append(s)
    continue
  for c in ("ACGT"):
    stack.append(s+c)

# dp["XXX"] : 直近3文字がXXXになっている場合の数のDP
dp={}
for b in buf:
  dp[b]=[0 for i in range(N+1)]
  if b not in ("AGC","ACG","GAC"):
    dp[b][3]=1

# ある3文字に対して次に来てはいけない文字
NG={
  "ACG":"C",
  "AGG":"C",
  "ATG":"C",
  "AGA":"C",
  "AGT":"C"
}
DIV=10**9+7

for i in range(3,N):
  for item in dp.items():
    key=item[0]
    value=item[1]
    ngnex=""
    if key in NG:
      ngnex=NG[key]
    las2=key[1:]
    for c in ("ACGT"):
      if las2+c in ("AGC","ACG","GAC"):
        continue
      if c!=ngnex:
        dp[las2+c][i+1]+=dp[key][i]
        dp[las2+c][i+1]%=DIV

ans=0
for v in dp.values():
  ans+=v[-1]
print(ans%DIV)