from itertools import product
n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for i in range(n)]
print(max([sum(sorted([i[0]*l[0]+i[1]*l[1]+i[2]*l[2] for l in xyz],reverse=True)[:m]) for i in product([-1,1],[-1,1],[-1,1])]))