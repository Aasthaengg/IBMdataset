from sys import stdin
def input():
    return stdin.readline().strip()

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()) - 1)

now = 0
ans = 0
for _ in range(n):
    now = l[now]
    ans += 1
    if now == 1:
        print(ans)
        exit()
else:
    print(-1)