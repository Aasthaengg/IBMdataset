n = int(input())
p = list(map(int ,input().split()))

t = sorted(p)
s = 0
for i in range(n):
    if p[i] != t[i]:
        s += 1

if s > 2:
    print("NO")
else:
    print("YES")