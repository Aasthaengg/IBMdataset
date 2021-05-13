n = int(input())
A = list(map(int, input().split()))
ans = []
maxa = max(A)
mina = min(A)
if abs(mina) > abs(maxa):
    for i in range(n)[:0:-1]:
        if A[i-1] > A[i]:
            while A[i-1] > A[i]:
                ma = min(A)
                argmina = A.index(ma)
                A[i-1] += ma
                ans.append((argmina+1, i-1+1))
else:
    for i in range(n-1):
        pa = A[i]
        aa = A[i+1]
        if pa > aa:
            while pa > A[i+1]:
                ma = max(A)
                argmaxa = A.index(ma)
                A[i+1] += ma
                ans.append((argmaxa+1, i+1+1))

print(len(ans))
for a in ans:
    print(*a)
