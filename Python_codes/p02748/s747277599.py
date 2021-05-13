import sys
input = sys.stdin.readline

a, b, m = [int(w) for w in input().split()]
a_li = [int(w) for w in input().split()]
b_li = [int(w) for w in input().split()]

ans = min(a_li) + min(b_li)

for i in range(m):
    x, y, c = [int(w) for w in input().split()]
    t = a_li[x - 1] + b_li[y - 1] - c
    ans = min(ans, t)

print(ans)
