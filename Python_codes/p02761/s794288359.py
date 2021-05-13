n, m = map(int, input().split())

ans = [-1] * n

for _ in range(m):
    s, c = map(int, input().split())
    if ans[s - 1] == -1:
        ans[s - 1] = c
    elif ans[s - 1] != -1 and ans[s - 1] != c:
        print(-1)
        exit()

if n != 1 and ans[0] == 0:
    print(-1)
    exit()

if n != 1 and ans[0] == -1:
    ans[0] = 1

for i in range(n):
    if ans[i] == -1:
        ans[i] = 0

print(''.join(map(str, ans)))
