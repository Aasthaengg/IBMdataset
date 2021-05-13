N, K = map(int, input().split())
h = list(map(int, input().split()))
rps = ['r', 's', 'p']
T = input()
ans = 0
for i in range(3):
    for j in range(K):
        o = True
        for k in range(j, N, K):
            if o and (rps[i]+T[k] == 'rs' or rps[i]+T[k] == 'sp' or rps[i]+T[k] == 'pr'):
                ans += h[i]
                o = False
            else:
                o = True
print(ans)
