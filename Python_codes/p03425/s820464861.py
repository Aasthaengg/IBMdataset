import itertools
N=int(input())
l=[0]*5
m=list('MARCH')
for i in range(N):
    S=input()
    if S[0] in m:
        l[m.index(S[0])]+=1
ans=0
for i in list(itertools.combinations(l,3)):
    m=1
    for j in i:
        m*=j
    ans+=m
print(ans)