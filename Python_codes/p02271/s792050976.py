import itertools as ite

n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))
x = []

for i in range(n):
    for j in list(ite.combinations(a,i+1)):
        x.append(sum(j))
for i in range(q):
    flag = 0
    for j in x:
        if m[i] == j:
            print("yes")
            flag = 1
            break
    if flag == 0: print("no")


