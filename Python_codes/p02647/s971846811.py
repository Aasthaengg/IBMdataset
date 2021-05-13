n,k = map(int, input().split())
A = list(map(int, input().split()))

for i in range(k):
    imo = [0] * (n + 1)
    for j in range(n):
        tmp = j-A[j]
        if tmp < 0:
            tmp = 0
        imo[tmp] += 1
        tmp2 = j+A[j]+1
        if tmp2 > n:
            tmp2 = n
        imo[tmp2] -=1
    if imo[0] == n and imo[n] == -n:
        A = [n] * n
        A = map(str, A)
        print(' '.join(A))
        exit()
    else:
        temp = 0
        for k in range(n):
            temp += imo[k]
            A[k] = temp
A = map(str, A)
print(' '.join(A))
