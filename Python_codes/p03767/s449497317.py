N = int(input())
A = [int(i) for i in input().split()]
sorted_A = sorted(A, reverse=True)

print(sum(sorted_A[1:2*N:2]))