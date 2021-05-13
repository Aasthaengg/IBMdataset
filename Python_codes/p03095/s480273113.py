n=int(input())
ss=list(input())
mod=10**9+7
import collections

"""
ss=[s[0]]

for i in range(1,n):
    if s[i]!=s[i-1]:
        ss.append(s[i])
"""
#print(ss)

c = collections.Counter(ss)

result=1
for k in c.keys():
    result=result*(c[k]+1)%mod

print((result-1)%mod)


