N = int(input())
D = sorted([int(input()) for _ in range(N)])
cnt = 1
d = D[0]
for i in range(1,N):
    if D[i]>d:
        cnt += 1
        d = D[i]
print(cnt)