N, A, B = list(map(int, input().split()))
X = [0] * N
for i in range(N):
    X[i] = int(input())

def C(x):
    Y = [0] * N
    for i in range(N):
        Y[i] = X[i] - x * B
    
    cnt = 0
    for i in range(N):
        if Y[i] > 0:
            cnt += (Y[i] + A - B - 1) // (A - B)
    return cnt <= x

ng = 0; ok = 10**18
while ok - ng > 1:
    mid = (ng + ok) >> 1
    if C(mid): ok = mid
    else: ng = mid

print(ok)