N = int(input())

A = list(map(int, input().split()))
B = 0
C = 1

if 0 in A:
    print(0)
    exit()

for i in range(N):
    C = C * A[i]
    if C > 1000000000000000000:
        print(-1)
        exit()

print(C)