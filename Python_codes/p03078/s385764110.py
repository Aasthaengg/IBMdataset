X,Y,Z,K = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse=1)
B = sorted(list(map(int,input().split())),reverse=1)
C = sorted(list(map(int,input().split())),reverse=1)
def solve(P):
    count = 0
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if (A[i]+B[j]+C[k]) < P:
                    break
                count += 1
                if count >= K:
                    return True
    return False

maxa = A[0]+B[0]+C[0]+1
mina = 0

while maxa -mina > 1:
    mid = (maxa+mina)//2
    if solve(mid):
        mina = mid
    else:
        maxa = mid
ans = []
for i in range(X):
    for j in range(Y):
        for k in range(Z):
            if (A[i]+B[j]+C[k]) < mina:
                break
            ans.append(A[i]+B[j]+C[k])

ans.sort(reverse=1)
for i in range(K):
    print(ans[i])
