import itertools
N_List = list(map(int,input().split()))
a = sum(N_List)

for v in itertools.combinations(N_List,2):
    if a >= sum(v):
        a = sum(v)
print(a)