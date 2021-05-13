n, m = map(int,input().split())
A = [list(map(int,input().split())) for i in range(m)]

B = [0] * (n+1)

for i in range(m):
    B[A[i][0]] += 1
    B[A[i][1]] += 1

no = 0
for i in range(1, n+1):
    if B[i] % 2 == 1:
        no = 1
        break

if no == 0:
    print("YES")
else:
    print("NO")