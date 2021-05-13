n = int(input())
A = list(map(int,input().split()))
B = A.copy()
A_max = max(A)
ans = 100

for i in range(n):
    if B[i] > A_max // 2:
        B[i] = A_max-B[i]

B.sort()
if B[-1] in A:
    print(str(A_max)+" "+str(B[-1]))
else:
    print(str(A_max)+" "+str(A_max-B[-1]))