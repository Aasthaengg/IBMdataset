import copy
N,M = map(int,input().split())
num = {}
tmp ={}
tmpli = []
li = []
p = []
count = 0
for i in range(M):
    for i in range(N):
        num[i+1] = 0
    a = list(map(int,input().split()))
    for j in range(len(a)-1):
        if a[j+1] in num:
            num[a[j+1]] += 1
    li.append(num.copy())
p = list(map(int,input().split()))

for i in range(2**N):
    tmpli = copy.deepcopy(li)
    for j in range(N):
        if ((i >> j) & 1):
            for k in tmpli:
                if j + 1 in k:
                    k[j+1] = 0
    tmp = 0
    for b in range(len(p)):
        if sum(tmpli[b].values()) % 2 == p[b]:
            tmp += 1
    if tmp == len(p):
        count += 1
print(count)