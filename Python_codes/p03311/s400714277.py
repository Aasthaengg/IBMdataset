N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    B.append(A[i] - i + 1)

B = sorted(B)
mid = B[N // 2]
num = 0
for i in range(N):
    num += abs(B[i] - mid)

print(num)