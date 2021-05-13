N = int(input())
A = list(map(int, input().split()))
xa, a = max(enumerate(A), key=lambda x: abs(x[1]))
print(2*N)
for i in range(2):
    print(xa+1, 1 if a > 0 else N)
if a > 0:
    for i in range(1, N):
        for j in range(2):
            print(i, i+1)
else:
    for i in range(N, 1, -1):
        for j in range(2):
            print(i, i-1)