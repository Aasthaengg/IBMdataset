MOD=10**9+7
N=int(input())
S=input()
cnt=[0]*26
for x in S:
    cnt[ord(x)-97]+=1
res=1
for i in range(26):
    res=res*(cnt[i]+1)%MOD
print(res-1)