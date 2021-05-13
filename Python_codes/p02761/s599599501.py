n, m = map(int, input().split())
a = [-1]*n
for i in range(m):
    s, c = map(int, input().split())
    if a[s-1] == -1:
        a[s-1] = c
    elif a[s-1] != c:
        print(-1)
        exit()
    if n != 1 and s == 1 and c == 0:
        print(-1)
        exit()
for i in range(n):
    if a[i] == -1:
        a[i] = 0
if n != 1 and a[0] == 0:
    a[0] = 1
for i in range(n):
    print(a[i], end="")