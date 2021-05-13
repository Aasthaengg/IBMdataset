h,w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))
ans = []
for i in range(n):
    for j in range(a[i]):
        ans.append(i+1)
for i in range(h):
    tar = ans[i * w:(i+1) * w]
    if i % 2 == 0:
        print(*tar)
    else:
        tar.reverse()
        print(*tar)


