N = int(input())
a = list(input().split())
A = [int(a[i]) for i in range(N)]
print(sum([A[i] - 1 for i in range(N)]))