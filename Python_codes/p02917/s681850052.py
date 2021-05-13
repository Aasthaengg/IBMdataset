N = int(input())
B = list(map(int, input().split()))
A = [0] * N
total = B[0] + B[-1]

for i in range(1, N-1):
    total += min(B[i], B[i-1])

print(total)
