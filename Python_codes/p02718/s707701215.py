N,M = map(int,input().split())
A = list(map(int,input().split()))
tot = sum(A)
if tot%(4*M)==0:
    a = tot//(4*M)
else:
    a = tot//(4*M)+1
cnt = 0
for i in range(N):
    if A[i]>=a:
        cnt += 1
if cnt>=M:
    print("Yes")
else:
    print("No")