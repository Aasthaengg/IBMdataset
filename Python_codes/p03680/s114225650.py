N, *A = map(int, open(0).read().split())

k = 0
for i in range(N):
    k = A[k]-1
    if k == 1:
        print(i+1)
        break
else:
    print(-1)
