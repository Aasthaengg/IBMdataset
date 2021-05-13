s = list(str(input()))
n = len(s)

dl = {'A':0, 'C':0, '?':0}
dr = {'A':0, 'C':0, '?':0}

dls = []
drs = []

import copy

for i in range(n):
    if s[i] == 'A' or s[i] == 'C':
        dl[s[i]] += 1
    elif s[i] == 'B':
        dl_ = copy.copy(dl)
        dls.append(dl_)
    else:
        dl_ = copy.copy(dl)
        dls.append(dl_)
        dl[s[i]] += 1
    j = n - 1- i
    if s[j] == 'A' or s[j] == 'C':
        dr[s[j]] += 1
    elif s[j] == 'B':
        dr_ = copy.copy(dr)
        drs.append(dr_)
    else:
        dr_ = copy.copy(dr)
        drs.append(dr_)
        dr[s[j]] += 1

drs = list(reversed(drs))
#print(dls)
#print(drs)

ans = 0
mod = 10**9+7

def power(a, n, mod):
  bi=str(format(n,"b")) #2進数
  res=1
  for i in range(len(bi)):
    res=(res*res) %mod
    if bi[i]=="1":
      res=(res*a) %mod
  return res

for i in range(len(dls)):
    a = (dls[i]['A']*power(3, dls[i]['?'], mod) + dls[i]['?']*power(3, max(0, dls[i]['?']-1), mod))%mod
    b = (drs[i]['C']*power(3, drs[i]['?'], mod) + drs[i]['?']*power(3, max(0, drs[i]['?']-1), mod))%mod
    ans += (a*b)%mod
    #print(ans)
ans %=mod
print(ans)