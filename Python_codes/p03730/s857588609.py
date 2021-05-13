import itertools
A, B, C = map(int,input().split())

lst = []
for i in range(1,100):
    lst.append(A * i)


for i in range(1,3):
    for v in itertools.combinations(lst,i):
        if sum(v) % B == C:
            print('YES')
            exit()
print('NO')