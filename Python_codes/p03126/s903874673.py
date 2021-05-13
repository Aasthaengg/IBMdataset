import collections

N, M = map(int, input().split())
koubutu = []
for _ in range(N):
    ka = list(map(int, input().split()))
    koubutu.extend(ka[1:])
print(list(collections.Counter(koubutu).values()).count(N))