import itertools
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
lis = [i for i in range(1,n+1)]
zisyo = list(itertools.permutations(lis))
print(abs(zisyo.index(tuple(p)) - zisyo.index(tuple(q))))