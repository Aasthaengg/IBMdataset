import itertools

n,m,q = map(int,input().split())
abcd = []
l = [i for i in range(1,m+1)]
h = itertools.combinations_with_replacement(l, n)
ans = 0

for i in range(q):
    abcd.append(list(map(int,input().split())))
for v in h:
    sum = 0
    for i in range(q):
        if v[abcd[i][1]-1] - v[abcd[i][0]-1] == abcd[i][2]:
            sum += abcd[i][3]
    ans = max(ans,sum)
print(ans)
