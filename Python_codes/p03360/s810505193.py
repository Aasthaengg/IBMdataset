A =  [int(i) for i in input().split()]
k = int(input())

print(max(A) * (2 ** k) + (sum(A) - max(A)))