from itertools import combinations_with_replacement

n,m,q = map(int,input().split())

L = [i+1 for i in range(m)]
li = [input().split() for i in range(q)]

for i in range(q):
    li[i] = [int(x) for x in li[i]]

ans = 0
for v in combinations_with_replacement(L,n):
    sum1 = 0
    for i in li:
        if v[i[1]-1] - v[i[0]-1] == i[2]:
            sum1 +=i[3]
    ans = max(ans,sum1)
print(ans)