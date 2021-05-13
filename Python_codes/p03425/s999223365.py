from collections import defaultdict
import sys
n=int(input())

d=defaultdict(int)
for i in range(n):
    s=input()
    d[s[0]]+=1

march=[d["M"],d["A"],d["R"],d["C"],d["H"]]
zero=march.count(0)
if zero>=3:
    ans=0
    print(ans)
    sys.exit()

m=[]
for i in march:
    if i>0:
        m.append(i)

ans=0
for i in range(len(m)-2):
    for j in range(i+1,len(m)-1):
        for k in range(j+1,len(m)):
            ans+=m[i]*m[j]*m[k]

print(ans)