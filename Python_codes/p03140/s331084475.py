N = int(input())
A = list(input())
B = list(input())
C = list(input())

ans = 0
for i in range(N):
    kind = len(set((A[i], B[i], C[i])))
    ans += kind - 1
print(ans)
