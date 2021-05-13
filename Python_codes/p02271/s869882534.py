from itertools import product

n = int(input())
A = map(int,input().split())
sums = set(map(sum,product(*((0,a) for a in A))))
q = int(input())
for m in map(int,input().split()):
    print('yes' if m in sums else 'no')
