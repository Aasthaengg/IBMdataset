N = int(input())
D = list(map(int, input().split()))

A = sum(D)**2 - sum([d*d for d in D])

print(A//2)