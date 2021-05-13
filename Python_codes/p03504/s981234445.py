import sys
from operator import itemgetter
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,c = map(int,readline().split())
ch = [[[0,0]] for _ in range(c)]
for i in range(n):
    s,t,c = map(int,readline().split())
    ch[c-1].append([s,t])
imos = [0]*(10**5+1)
for i in ch:
    i.sort()
    for j in range(1,len(i)):
        s,t = i[j]
        if i[j-1][1] < s:
            imos[s-1] += 1
        else:
            imos[s] += 1
        imos[t] -= 1

for i in range(1,len(imos)):
    imos[i] += imos[i-1]

print(max(imos))

