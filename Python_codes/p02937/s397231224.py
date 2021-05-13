from collections import Counter
import bisect

S = input()
T = input()

ls = len(S)
lt = len(T)

cons = Counter(S)
cont = Counter(T)
dics = {}
dicc = {}

for i in range(ls):
  if S[i] not in dics:
    dics[S[i]] = [i+1]
    dicc[S[i]] = 1
  else:
    dics[S[i]].append(i+1)
    dicc[S[i]] += 1
idx = 0
cic = 0
for t in T:
  if t not in dics:
    print(-1)
    exit()
  i = bisect.bisect_left(dics[t], idx)
  if i == dicc[t]:
    idx = dics[t][0] + 1
    cic += 1
  else:
    idx = dics[t][i] + 1
    
print(cic*ls+idx-1)