N = int(input())
A = input()
B = input()
C = input()
ans = 0
for i in range(N):
    if (A[i] is B[i]) & (A[i] is C[i]):
        ans += 0
    elif (A[i] is B[i]) | (B[i] is C[i]) | (A[i] is C[i]):
        ans += 1
    else:
        ans += 2
print(ans) 