n = int(input())
A = [*map(int, input().split())]
yen = 1000
for i in range(n-1): yen += max(0, yen//A[i] * (A[i+1] - A[i]))
print(yen)
