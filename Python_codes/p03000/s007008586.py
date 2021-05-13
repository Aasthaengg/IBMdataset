N, X = map(int,input().split())
L = list(map(int,input().split()))

D = [0]

ans = 1

for i in range(0,N):
    D.append(D[i]+L[i])
    if D[i+1] > X:
        break
    else:
        ans += 1

print(ans)
