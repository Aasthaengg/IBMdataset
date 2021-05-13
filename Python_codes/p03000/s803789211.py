N,X = map(int,input().split())
Ls = list(map(int,input().split()))

D = 0
ans = 1

for i in range(N):
    D += Ls[i]
    if D <= X:
        ans += 1
    else:
        break

print(ans)