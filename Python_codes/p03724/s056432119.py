n, m = map(int, input().split())
dat = [0] * (n+10)
for _ in range(m):
    a,b = map(int, input().split())
    dat[a] += 1
    dat[b] += 1
can = True
for i in range(n):
    if dat[i] % 2 == 1:
        can = False
print("YES" if can else "NO")