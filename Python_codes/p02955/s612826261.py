import sys
input = sys.stdin.readline
n, k = map(int,input().split())
A = list(map(int,input().split()))

s = sum(A)
D = []
for i in range(1, int(s**0.5) + 1):
    if s % i == 0:
        D.append(i)
        if i != s//i:
            D.append(s//i)
D.sort(reverse=True)

for i in range(len(D)):
    B = {}
    for j in range(n):
        try:
            B[A[j] % D[i]] += 1
        except:
            B[A[j] % D[i]] = 1
    C = list(B.items())
    C.sort()
    # print(D[i], C)
    E = []
    for j in range(len(C)):
        E.append([C[j][0], C[j][1]])
    nn = n
    c = 0
    
    l = 0
    r = len(E)-1
    ls = 0
    rs = 0
    while nn > 0:
        if ls <= rs:
            ls += E[l][0]
            E[l][1] -= 1
            nn -= 1
            if E[l][1] == 0:
                l += 1
        else:
            rs += D[i] - E[r][0]
            E[r][1] -= 1
            nn -= 1
            if E[r][1] == 0:
                r -= 1
    # print(ls,rs)
    if ls <= k:
        print(D[i])
        break