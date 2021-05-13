N = int(input())
Nmax1 = [0, 0]
Nmax2 = [0, 0]
A = []
for i in range(N):
    x = int(input())
    if Nmax1[0] <= x:
        Nmax2[0] = Nmax1[0]
        Nmax2[1] = Nmax1[1]
        Nmax1[0] = x
        Nmax1[1] = i
    elif Nmax2[0] < x:
        Nmax2[0] = x
        Nmax2[1] = i

ans = [Nmax1[0]]*N
ans[Nmax1[1]] = Nmax2[0]

for i in ans:
    print(i)
