n, m = map(int, input().split())
x = [-1] * n
for _ in range(m):
    s, c = map(int, input().split())
    s -= 1
    if x[s] != -1 and x[s] != c:
        print(-1)
        quit()
    x[s] = c
if n > 1 and x[0] == 0:
    print(-1)
    quit()

if x[0] == -1:
    x[0] = 1 if n > 1 else 0
for i in range(1, n):
    if x[i] == -1:
        x[i] = 0
print(''.join(map(str, x)))