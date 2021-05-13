h, w = map(int, input().split())
n = int(input())
list_A = list(map(int, input().split()))
ans = [[0]*w for _ in range(h)]
cnt = -1
x = []
y = []
for i in range(w):
    if i % 2 == 0:
        x += [i for i in range(h)]
    else:
        l = [i for i in range(h)]
        l.reverse()
        x += l

for i in range(w):
    for _ in range(h):
        y.append(i)

for i, num in enumerate(list_A):
    for _ in range(num):
        cnt += 1
        ans[x[cnt]][y[cnt]] = i+1

for l in ans:
    print(*l)