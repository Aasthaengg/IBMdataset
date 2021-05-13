from collections import defaultdict
n=int(input())
s=input()
mod=pow(10,9)+7
sd=defaultdict(lambda:1)
for i in range(n):
      sd[s[i]]+=1
ans=1
for k in sd.keys():
      ans*=(sd[k])%mod
print(ans%mod-1)
