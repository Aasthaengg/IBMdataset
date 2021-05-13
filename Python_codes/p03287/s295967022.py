
N,M = map(int,input().split())
A = list(map(int,input().split()))


#%%
import bisect

modlist = []
for a in A:
    modlist.append(a%M)
    
ruisekiwa = [0]*(N+1)

idict = {}
for i in range(N):
    ruisekiwa[i+1] = ruisekiwa[i] + modlist[i]
    ruisekiwa[i+1] %= M
    idict[ruisekiwa[i+1]] = 0

exists = []
for s in ruisekiwa[1:]:
    idict[s] += 1
    exists.append(s)

exists.sort()    
keys = list(idict.keys())
keys.sort()
ans = 0
for i in range(len(keys)):
    k = keys[i]
    if k == 0:
        ans += idict[k]*(idict[k]+1)//2
    else:
        ans += idict[k]*(idict[k]-1)//2
    
    
            
print(ans)
    
