n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
e = [0 for _ in range(n)]
for i in range(n):
    if d[i][0] == d[i][1]:
        e[i] = 1
f = [0 for _ in range(n)]
for i in range(2, n):
    f[i] = e[i]*e[i-1]*e[i-2]
if sum(f) > 0:
    print("Yes")
else:
    print("No")