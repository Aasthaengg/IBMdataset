N = int(input())
D = sorted([int(input()) for _ in range(N)],reverse=True)
d = D[0]
cnt = 1
for i in range(1,N):
    if D[i]<d:
        cnt += 1
        d = D[i]
print(cnt)