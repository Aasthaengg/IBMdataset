h,w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
res = []
for i in range(len(a)):
    res += [i+1]*a[i]

ans = [[0]*w for k in range(h)]
for i in range(h):
    for j in range(w):
        l = res.pop()
        ans[i][j] = l

for i in range(h):
    if(i%2==1):
        ans[i].reverse()
for i in range(h):
    print(*ans[i])