n,m = map(int,input().split())

li1 = [False] * n
lin = [False] * n

for _ in range(m):
    a,b = map(int,input().split())
    if a == 1:
        li1[b-1] = True
    elif b == n:
        lin[a-1] = True

for i in range(n):
    if li1[i] and lin[i]:
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')
