from itertools import accumulate
inf = float('inf')

def acc_max(array):
    na = []
    tmp = 0
    for a in array:
        if a > tmp:
            tmp = a
        na.append(tmp)
    return na

N,C = map(int,input().split())
X = []; V = []
for _ in range(N):
    x,v = map(int,input().split())
    X.append(x)
    V.append(v)

right = list(accumulate(V))
left = list(accumulate(V[::-1]))

right1 = [r - x for r, x in zip(right,X)]

left1 = [l - (C-x) for l, x in zip(left,X[::-1])]

right2 = acc_max([r - 2*x for r, x in zip(right,X)])

left2 = acc_max([l - 2*(C-x) for l, x in zip(left,X[::-1])])

ans = 0

for end in range(N):
    if end == N-1:
        res = max(right1[end],left1[end])
    else:
        res = max(right1[end]+left2[N-1-(end+1)],left1[end]+right2[N-1-(end+1)])
    if res > ans:
        ans = res

print(ans)