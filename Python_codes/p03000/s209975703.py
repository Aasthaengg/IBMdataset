N, X = map(int,input().split())
L = list(map(int,input().split()))
D = 0
cnt = 1

for i in range(N):
    D = D + L[i]
    if D > X:
        break
    cnt += 1

print(cnt)
