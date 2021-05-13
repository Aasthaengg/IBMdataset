n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]
na = len(A[0])
nb = len(B[0])
flag = False
for i in range(n-nb+1):
    for j in range(n-m+1):
        cnt = 0
        for a, b in zip(A[i:i+nb], B):
            if a[j:j+m] == b:
                cnt += 1
        if cnt == m:
            flag = True
            break
print('Yes' if flag else 'No')
