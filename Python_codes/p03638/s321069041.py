h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
ind = 0
ans = [[0 for i in range(w)] for j in range(h)]
for i in range(w):
    if i % 2 == 0:
        for j in range(h-1, -1, -1):
            if a[ind] == 0:
                ind += 1
            ans[j][i] = ind+1
            a[ind] -= 1

    else:
        for j in range(h):
            if a[ind] == 0:
                ind += 1
            ans[j][i] = ind+1
            a[ind] -= 1

for i in range(h):
    print(" ".join(map(str, ans[i])))
