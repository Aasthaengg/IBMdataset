import sys
input = sys.stdin.readline

lst = []
lst_append = lst.append
H, W, N = map(int, input().split())
tmplst = [-1, 0, 1]
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for i in tmplst:
        if 1 <= a + i <= H - 2:
            for j in tmplst:
                if 1 <= b + j <= W - 2:
                    lst_append((a + i, b + j))

lst.sort()
ans = [0] * 10
ans[0] = (H - 2) * (W - 2)

tmp = None
count = 0
for i in lst:
    if i == tmp:
        count += 1
    else:
        ans[0] -= 1
        ans[count] += 1
        count = 1
        tmp = i

ans[0] -= 1
ans[count] += 1
print (*ans, sep = '\n')