N, M = map(int, input().split())
l = [False]*N
for _ in range(M):
    a = list(map(int, input().split()))
    j = [1,N]
    for i in [0,1]:
        if a[i] == j[i]:
            if l[a[1-i]-1]:
                print('POSSIBLE')
                exit()
            else:
                l[a[1-i]-1] = True
print('IMPOSSIBLE')
