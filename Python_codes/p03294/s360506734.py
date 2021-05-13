n = int(input())

A = list(map(int, input().split()))

print(sum(n - 1 for n in A))