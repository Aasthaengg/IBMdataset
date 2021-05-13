N,K = map(int,input().split())
V = [0] + list(map(int,input().split())) + [0]
m = min(N,K)

A = []
ans = 0

#左からi個、右からj個除いた時の宝石の価値のmax

for i in range(m+1):
    if i == 0:
        pass
    else:
        A.append(V[i])
    B = []
    for j in range(m-i+1):
        if j == 0:
            pass
        else:
            B.append(V[N-j+1])
        C = A+B
        C.sort()
        a = sum(C)
        for k in range(len(C)):
            if C[k] < 0 and k < K-(i+j):
                a -= C[k]
        ans = max(ans,a)

print(ans)