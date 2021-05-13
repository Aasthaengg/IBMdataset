h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
lis = []

for i in range(n):
    lis.append([a[i],i+1])
#print(lis)
ans = [[0] * w for i in range(h)]
for i in range(h):
    for j in range(w):
        if lis[0][0] == 0:
            del lis[0]
        ans[i][j] = lis[0][1]
        lis[0][0] -= 1
for i in range(h):
    if i % 2 != 0:
        ans[i].reverse()
for i in range(h):
    print(' '.join(map(str,ans[i])))