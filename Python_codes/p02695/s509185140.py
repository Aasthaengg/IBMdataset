import copy

def cnt(a, m, i):
    if a[i] < m:
        a[i] += 1
    else:
        a = cnt(a, m, i-1)
        a[i] = copy.deepcopy(a[i-1])
    return a

def check(a, ab):
    score = 0
    for i in range(q):
        ai, bi = ab[i][0], ab[i][1]
        if a[bi] - a[ai] == ab[i][2]:
            score += ab[i][3]
    return score
  
n, m, q = map(int,input().split())
ab = []
for i in range(q):
    ab.append(list(map(int,input().split())))

a = [1] * (n+1)
a[0] = 0
ans = 0
while a[0] == 0:
    x = check(a, ab)
    ans = max(ans, x)
    # print(a, ans)
    a = cnt(a, m, -1)
print(ans)
