import itertools
N,X=map(int,input().split())
L=[int(x) for x in input().split()]
ans=sum(x<=X for x in itertools.accumulate([0]+L))
print(ans)
