h,w = map(int,input().split())
n = int(input())
a = [int(i) for i in input().split()]
ans = [[0 for _ in range(w)] for _ in range(h)]
cnt = 0
idx = 0
color = 1

for i in range(h):
    for j in range(w):
        cnt += 1
        if i%2 == 0:
            ans[i][j] = color
        else:
            ans[i][w-1-j] = color
        if cnt == a[idx] and idx != n-1:
                cnt = 0
                idx += 1
                color += 1

for i in range(h):
    for j in range(w):
        if j != w-1:
            print(ans[i][j],end=" ")
        else:
            print(ans[i][j])