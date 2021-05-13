import itertools
n,m,q = map(int, input().split())
p=[[0,0,0,0]]
for i in range(q):
    p.append(list(map(int, input().split())))

ans=0

for tmp in itertools.combinations_with_replacement(range(1,m+1),n):
    tokuten=0
    for gyou in range(1,q+1):
        if tmp[p[gyou][1]-1]-tmp[p[gyou][0]-1]==p[gyou][2]:
            tokuten+=p[gyou][3]
    ans=max(ans,tokuten)

print(ans)