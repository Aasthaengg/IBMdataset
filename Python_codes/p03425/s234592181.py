import itertools
N=int(input())
s=set(["M","A","R","C","H"])
d=dict(zip(list(s),[0]*5))
for _ in range(N):
    try:
        d[input()[0]]+=1
    except KeyError:
        pass
ans=0
for v in itertools.combinations(d.keys(), 3):
    ans+=d[v[0]]*d[v[1]]*d[v[2]]

print(ans)
#S=[input() for _ in range(N) if input()[0] in s]
