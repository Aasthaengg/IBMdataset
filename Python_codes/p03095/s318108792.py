from collections import Counter
n = int(input())
S = input()
mod = pow(10,9)+7
cS = Counter(list(S))
ans = 1
for key in cS.keys():
    ans *= (cS[key]+1)%mod
print((ans-1)%mod)