A = list(map(int, input().split()))
K = int(input())
print(max(A)*(2**K)+sum(A)-max(A))