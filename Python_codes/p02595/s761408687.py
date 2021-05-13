nd = input().split()
N = int(nd[0])
D = int(nd[1])
D = D**2

ans = 0

for i in range(N):
    ls = input().split()
    x = int(ls[0])
    y = int(ls[1])
    d = x**2 + y**2
    if d <= D :
        ans += 1

print(ans)
