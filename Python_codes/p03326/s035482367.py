import itertools   
x,y = map(int,input().split())
ab = []
for _ in range(x):
    a, b, c = (int(x) for x in input().split())
    ab.append([a, b, c])
ans = -1000000000000000000000
for i in itertools.product([1,-1], repeat=3):
    memo = []
    ansl = 0
    for j in ab:
        p = j[0]*i[0]+j[1]*i[1]+j[2]*i[2]
        memo.append(p)
    memo.sort(reverse=True)
    for k in range(y):
        ansl += memo[k]
    ans = max(ans, ansl)
print(ans)