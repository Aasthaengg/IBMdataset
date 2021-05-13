import collections
N=int(input())
lis=[''.join(sorted(input(), key=str.upper)) for _ in range(N)]
v=collections.Counter(lis).values()
ans=sum(list(map(lambda x: x*(x-1)//2, v)))
print(ans)