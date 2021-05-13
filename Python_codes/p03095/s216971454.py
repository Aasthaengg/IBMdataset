N=int(input())
S=input()
MOD=10**9+7
ALP='qazwsxcedrfvtgbyhnujmikolp'
cnt={}
for s in ALP:
  cnt[s]=0
for s in S:
  cnt[s]+=1
ans=1
for s in ALP:
  ans*=cnt[s]+1
ans-=1
print(ans%MOD)