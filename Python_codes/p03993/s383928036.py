N = int(input())
A = [int(i) - 1 for i in input().split()]
print(len([1 for i, a in enumerate(A) if i == A[a] and i < a]))