N,K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))

A.sort()
F.sort(reverse=True)

ok = A[-1] * F[0]
ng = 0

while ok-ng>1:
    mid = (ok+ng)//2
    trainings = 0
    for i in range(N):
        t = A[i]-mid//F[i]
        if t > 0:
            trainings += t
    if trainings <= K:
        ok = mid
    else:
        ng = mid
trainings = 0
for i in range(N):
    t = A[i]-ng//F[i]
    if t>0:
        trainings += t
if trainings<=K:
    print(ng)
else:
    print(ok)