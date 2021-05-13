import itertools,math
n = int(input())
a = sorted(list(itertools.permutations([ i for i in range(1,n+1)])))
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))
print(abs(a.index(p) - a.index(q)))