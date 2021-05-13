N = int(input())
A = input()
B = input()
C = input()
s = set()
res = 0

for i in range(N):
    s.add(A[i])
    s.add(B[i])
    s.add(C[i])
    res += len(s)-1
    s.clear()
print(res)
