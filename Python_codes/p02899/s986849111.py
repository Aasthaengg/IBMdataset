n = int(input())
A = list(map(int, input().split()))

D = {}
for i in range(1, n+1):
    D[A[i-1]] = i

for k, v in sorted(D.items()):
    print(v, end=" ")