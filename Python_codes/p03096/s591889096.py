import sys
input = sys.stdin.readline
mod = 10**9 +7
N = int(input())
C = [input() for _ in range(N)]
dic ={}
lis = [1]
before =C.pop(0)
dic[before]=[0]

for i,s in enumerate(C):
    lis.append(lis[-1])
    if s in dic.keys():
        if s != before:
            lis[-1] += lis[dic[s][-1]+1]
            #for j in dic[s]:
            #    lis[-1] += lis[j]
            dic[s].append(i)
    else:
        dic[s] = [i]
    before = s
    lis[-1] = lis[-1]%mod
print(lis[-1])