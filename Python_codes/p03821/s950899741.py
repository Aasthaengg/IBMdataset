n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
cnt = 0
for i in range(n-1, -1, -1):
    t = (A[i]+cnt) % B[i]
    if t!=0:
        cnt += (B[i]-t)

print(cnt)