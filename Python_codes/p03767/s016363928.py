N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

print(sum(A[i] for i in range(1, 2 * N + 1, 2)))
