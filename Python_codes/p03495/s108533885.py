import collections
N,K = (int(T) for T in input().split())
A = collections.Counter([int(T) for T in input().split()]).most_common()
Num,Count = zip(*A)
if len(Num)<=K:
    print(0)
else:
    print(N-sum(Count[:K]))