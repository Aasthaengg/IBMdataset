N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A = list(sorted(A))
print(sum(A) - (A[-1] // 2))
