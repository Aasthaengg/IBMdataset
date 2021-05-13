N = int(input())
A = [int(a) for a in input().split()]
A.sort(reverse=True)
print(sum(A[1:N * 2 + 1:2]))