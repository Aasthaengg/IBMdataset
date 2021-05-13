from itertools import permutations
n=int(input())
p,q = tuple(map(int, input().split())), tuple(map(int, input().split()))
l = list(range(1,n+1))
x = [i for i in permutations(l,n)]
print(abs(x.index(p) - x.index(q)))