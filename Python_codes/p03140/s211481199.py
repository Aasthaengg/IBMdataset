N = int(input())
A = str(input())
B = str(input())
C = str(input())
ans = 0
for i in range(0, N):
    tmp = set()
    tmp.add(A[i])
    tmp.add(B[i])
    tmp.add(C[i])
    ans += (len(tmp)-1)
print(ans)
