N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append((a,b))
    B.append((i,a+b))
B.sort(key=lambda x:x[1], reverse=True)
res = 0
for i, _ in B[::2]:
    res += A[i][0]
for i, _ in B[1::2]:
    res -= A[i][1]
print(res)